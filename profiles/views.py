# 3rd party imports
# Django imports
from django.shortcuts import render

# Local imports
from products.models import (
                    Product,
                    Category,
                    ProductReview)


def profile(request):
    """
    """
    context = {}

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