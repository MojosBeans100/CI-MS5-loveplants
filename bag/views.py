# 3rd party imports

# Django imports
from django.contrib import messages
from django.shortcuts import render, redirect, reverse

# Local imports
from products.models import Product, ProductReview


def view_bag(request):
    """
    A view to render the contents of the basket
    """
    liked_products_list = []
    if request.user.is_authenticated:

        liked_products = ProductReview.objects.filter(user=request.user,
                                                      liked=True)
        for i in liked_products:
            liked_products_list.append(i.product.friendly_name)

    context = {
        'liked_list': liked_products_list
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """
    A view to add items to the basket
    """

    items_in_stock = Product.objects.get(id=item_id).stock_quantity
    product = Product.objects.get(id=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    add_message = f'Added {quantity} x "{product.friendly_name}" to basket'
    bag = request.session.get('bag', {})

    if quantity > items_in_stock:
        message = "There are not enough items in stock:"
        " please choose a smaller quantity"
        print(message)
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, add_message, extra_tags='bag')
        else:
            bag[item_id] = quantity
            messages.success(request, add_message, extra_tags='bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """
    A view to edit the contents of the basket
    """

    items_in_stock = Product.objects.get(id=item_id).stock_quantity
    product = Product.objects.get(id=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    for i in bag:
        if i == item_id:
            old_value = bag[i]

    edit_message = (f'Updated quantity of "{product.friendly_name}"'
                    f' from {old_value} to {quantity}')
    remove_message = (f'Removed {quantity} of '
                      f'{product.friendly_name} from basket')

    if quantity > items_in_stock:
        message = "There are not enough items in stock: "
        "please choose a smaller quantity"
        print(message)
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, edit_message, extra_tags='bag')
        else:
            bag.pop(item_id)
            messages.success(request, remove_message, extra_tags='bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def delete_bag(request, item_id):
    """
    A view to delete an item from the basket
    """

    delete_product = Product.objects.get(pk=item_id)
    bag = request.session.get('bag', {})
    bag.pop(item_id)

    remove_product_message = (f"Removed {delete_product.friendly_name} "
                              f"from bag.")

    messages.success(request,
                     remove_product_message,
                     extra_tags='bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
