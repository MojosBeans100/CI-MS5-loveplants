# 3rd party imports

# Django imports
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Local imports
from .models import Order
from .forms import OrderForm


def view_checkout(request):
    """
    """

    bag = request.session.get('bag', {})

    # if not bag:
    #     messages.error(request, "There's nothing in your bag at the moment.")
        #return redirect(reverse('products'))

    order_form = OrderForm()

    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context)
