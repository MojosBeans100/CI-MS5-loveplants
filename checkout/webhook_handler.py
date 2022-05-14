# 3rd party imports
import json
import time

# Django imports
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# Local imports
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile


class StripeWH_Handler:
    """
    Handle Stripe webhooks for order redundancy
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email of their order
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}", status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook event
        """

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount/100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_num = shipping_details.phone
                profile.default_town_or_city = shipping_details.address.city
                profile.default_country = shipping_details.address.country
                x = shipping_details.address.line1
                y = shipping_details.address.line2
                profile.default_street_address_1 = x
                profile.default_street_address_2 = y
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1

        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_num__iexact=shipping_details.phone,
                    town_or_city__iexact=shipping_details.address.city,
                    country__iexact=shipping_details.address.country,
                    street_address_1__iexact=shipping_details.address.line1,
                    street_address_2__iexact=shipping_details.address.line2,
                    postcode__iexact=shipping_details.address.postal_code,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    stripe_pid=pid,
                    original_bag=bag,
                )

                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} |'
                    f' success: verified order already created',
                    status=200
                )

        else:
            order = None
            try:
                order = Order.objects.create(
                        full_name=shipping_details.name,
                        user_profile=profile,
                        email=billing_details.email,
                        phone_num=shipping_details.phone,
                        town_or_city=shipping_details.address.city,
                        country=shipping_details.address.country,
                        street_address_1=shipping_details.address.line1,
                        street_address_2=shipping_details.address.line2,
                        postcode=shipping_details.address.postal_code,
                        county=shipping_details.address.state,
                        stripe_pid=pid,
                        original_bag=bag,
                    )

                for item_id, quantity in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f"Webhook received: "
                                    f"{event['type']}"
                                    f"| error {e}", status=500)

        self._send_confirmation_email(order)
        return HttpResponse(
            content=f"Webhook received: {event['type']}"
            f" | Success: created order in webhook!", status=200)

    def handle_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook event
        """

        return HttpResponse(
            content=f"Webhook received: {event['type']}", status=200)
