
# import Django
from django.shortcuts import render

# import local
from products.models import Product


def all_products(request):
    """
    """

    all_products = Product.objects.all()

    context = {
        'all_products': all_products
    }

    return render(request, 'products/products.html', context)


def product_detail(request, id):
    """
    """

    product = Product.objects.get(id=id)

    if product.rare is True:
        rare_products = Product.objects.filter(rare=True).exclude(id=id)

    if product.popular is True:
        popular_products = Product.objects.filter(popular=True).exclude(id=id)

    context = {
        'product': product,
        'rare_products': rare_products,
        'popular_products': popular_products,
    }

    return render(request, 'products/product_detail.html', context)

