
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

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)

