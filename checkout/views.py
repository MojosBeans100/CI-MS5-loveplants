# 3rd party imports
import stripe
import json

# Django imports
from django.shortcuts import (render,
                              redirect,
                              reverse,
                              get_object_or_404)
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.http import require_POST

# Local imports
import os
from .models import Order, OrderLineItem
from products.models import Product
from .forms import OrderForm
from bag.contexts import bag_contents

stripe_pk = os.environ.get('STRIPE_PUBLIC_KEY')
stripe_sk = os.environ.get('STRIPE_SECRET_KEY')


@require_POST
def cache_checkout_data(request):
    """
    """

    post_data = json.loads(request.body.decode("utf-8"))
    try:
        pid = post_data['stripe_sk'].split('_secret')[0]
        stripe.api_key = stripe_sk
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry your payment could not be completed')
        return HttpResponse(content=e, status=400)


def view_checkout(request):
    """
    A view to render the checkout page and handle payment
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

            # remember to remove items from stock

            order_form.save()
            order = order_form.save(commit=False)

            for item_id, quantity in bag.items():

                product = Product.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                )
                order_line_item.save()

                # product.stock_quantity = product.stock_quantity - quantity
                # product.save()

            return redirect(reverse(
                            'checkout_success',
                            args=[order.order_ref]))

        else:
            messages.error(request, 'There is an error in the form')

    else:
        bag = request.session.get('bag', {})

        if not bag:
            messages.error(request, "There's nothing"
                                    " in your bag at the moment.")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        current_total = current_bag['grand_total']
        stripe_total = round(current_total*100)
        stripe.api_key = stripe_sk
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='gbp',
        )

        order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_pk': stripe_pk,
        'stripe_sk': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_ref):
    """
    A view to display order details when checkout is successful
    """

    order = get_object_or_404(Order, order_ref=order_ref)
    order_line_items = OrderLineItem.objects.filter(order=order)
    messages.success(request, f'{order} has been successful')

    if 'bag' in request.session:
        del request.session['bag']

    context = {
        'order': order,
        'line_items': order_line_items,
    }

    return render(request, 'checkout/checkout_success.html', context)
