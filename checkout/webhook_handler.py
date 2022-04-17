# 3rd party imports
import json

# Django imports
from django.http import HttpResponse

# Local imports
from .models import Order, OrderLineItem
from products.models import Product


class StripeWH_Handler:
    """
    Handle Stripe webhooks for order redundancy
    """

    # class of set up method that's called every time an instance
    # of the class is created
    def __init__(self, request):
        self.request = request

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

        # check this - does this work?
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False

        # see if this order has been created already
        try:
            order = Order.objects.get(
                full_name__iexact=shipping_details.name,
                email__iexact=billing_details.email,
                phone_num__iexact=shipping_details.phone,
                town_or_city__iexact=shipping_details.city,
                country__iexact=shipping_details.country,
                street_address_1__iexact=shipping_details.line1,
                street_address_2__iexact=shipping_details.line2,
                postcode__iexact=shipping_details.postal_code,
                county__iexact=shipping_details.state,
                grand_total=grand_total,
            )

            # if order exists, return
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | success: verified order already created',
                status=200
            )

        # if order does not exist, create line items
        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                        full_name=shipping_details.name,
                        email=billing_details.email,
                        phone_num=shipping_details.phone,
                        town_or_city=shipping_details.city,
                        country=shipping_details.country,
                        street_address_1=shipping_details.line1,
                        street_address_2=shipping_details.line2,
                        postcode=shipping_details.postal_code,
                        county=shipping_details.state,
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
                return HttpResponse(content=f"Webhook received: {event['type']} | error {e}",
                status=500)

        return HttpResponse(
            content=f"Webhook received: {event['type']}", status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook event
        """

        return HttpResponse(
            content=f"Webhook received: {event['type']}", status=200)
