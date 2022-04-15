# 3rd party imports
import stripe

# Django imports
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

# Local imports
import os
from .models import Order, OrderLineItem
from products.models import Product
from .forms import OrderForm
from bag.contexts import bag_contents

stripe_pk = os.environ.get('STRIPE_PUBLIC_KEY')
stripe_sk = os.environ.get('STRIPE_SECRET_KEY')


def view_checkout(request):
    """
    """

    if request.method == 'POST':

        bag = request.session.get('bag', {})
        form_info = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_num': request.POST['phone_num'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_info)

        if order_form.is_valid():
            order_form.save()
            order = order_form.save(commit=False)

            for item_id, item_data in bag.items():

                product = Product.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=item_data,
                )
                order_line_item.save()

            return redirect(reverse(
                            'checkout_success',
                            args=[order.order_number]))

        else:
            messages.error(request, 'There is an error in the form')

    else:

        bag = request.session.get('bag', {})

        # if not bag:
        #     messages.error(request, "There's nothing in your bag at the moment.")
            #return redirect(reverse('products'))

        current_bag = bag_contents(request)
        current_total = current_bag['grand_total']
        stripe_total = round(current_total*100)
        stripe.api_key = stripe_sk
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='gbp',
        )

        print(intent)

        order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_pk': stripe_pk,
        'stripe_sk': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)
