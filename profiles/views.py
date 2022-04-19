# 3rd party imports

# Django imports
from django.shortcuts import render, get_object_or_404

# Local imports
from products.models import (
                    Product,
                    ProductReview
                    )
from checkout.models import (
                    Order,
                    OrderLineItem
                    )
from .models import UserProfile, User
from .forms import UserProfileForm


def profile(request):
    """
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    line_items = OrderLineItem.objects.all()
    dropdowns = []
    hrefs = []
    i = 1

    while i <= len(orders):
        dropdown_label = f"multiCollapseExample{i}"
        href = f"#multiCollapseExample{i}"
        dropdowns.append(dropdown_label)
        hrefs.append(href)
        i += 1

    for j in line_items:
        print(type(j.order.order_ref))
        
    for k in orders:
        print(type(k.order_ref))

    context = {
        'form': form,
        'orders': orders,
        'dropdowns': dropdowns,
        'hrefs': hrefs,
        'line_items': line_items,
    }

    return render(request, 'profiles/profile.html', context)


def liked_products(request):
    """
    """

    all_products = Product.objects.all()
    liked_products_list = []

    if request.user.is_authenticated:
        liked_products = ProductReview.objects.filter(user=request.user,
                                                      liked=True)
        for i in liked_products:
            liked_products_list.append(i.product.friendly_name)

    context = {
        'liked': liked_products_list,
        'products': all_products,
        'num_liked': len(liked_products_list),
    }

    return render(request, 'profiles/liked.html', context)