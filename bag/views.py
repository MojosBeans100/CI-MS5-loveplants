from django.shortcuts import render, redirect, reverse
from products.models import Product
from django.contrib import messages


def view_bag(request):
    """
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    """

    items_in_stock = Product.objects.get(id=item_id).stock_quantity

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if quantity > items_in_stock:
        message = "There are not enough items in stock: please choose a smaller quantity"
        print(message)
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)


def edit_bag(request, item_id):

    items_in_stock = Product.objects.get(id=item_id).stock_quantity
    product = Product.objects.get(id=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > items_in_stock:
        message = "There are not enough items in stock: please choose a smaller quantity"
        print(message)
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated quantity of {product.friendly_name} to {quantity}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {quantity} of from basket')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
