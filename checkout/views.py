# 3rd party imports
import stripe

# Django imports
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

# Local imports
import os
from .models import Order
from .forms import OrderForm
from bag.contexts import bag_contents

stripe_pk = os.environ.get('STRIPE_PUBLIC_KEY')
stripe_sk = os.environ.get('STRIPE_SECRET_KEY')


def view_checkout(request):
    """
    """

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
