from django.shortcuts import render, redirect, reverse
from products.models import Product


def view_bag(request):
    """
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    """

    items_in_stock = Product.objects.get(id=item_id).stock_quantity
    print(items_in_stock)

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
    print(request.session['bag'])

    return redirect(redirect_url)


def edit_bag(request, item_id):

    items_in_stock = Product.objects.get(id=item_id).stock_quantity
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > items_in_stock:
        message = "There are not enough items in stock: please choose a smaller quantity"
        print(message)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
