
# import Django
from django.shortcuts import render
from django.db.models import Q

# import local
from products.models import Product


def all_products(request):
    """
    """

    all_products = Product.objects.all()

    if 'q' in request.GET:
        search_query = request.GET['q']
        # if not search_query:

        search_queries = Q(name__icontains=search_query) | Q(description__icontains=search_query)
        all_products = all_products.filter(search_queries)

    context = {
        'all_products': all_products
    }

    return render(request, 'products/products.html', context)


def product_detail(request, id):
    """
    """

    product = Product.objects.get(id=id)

    if product.rare is True:
        rare_products = Product.objects.filter(rare=True).exclude(id=id)[0:4]
    else:
        rare_products = ""

    if product.popular is True:
        popular_products = Product.objects.filter(popular=True).exclude(id=id)[0:4]
    else:
        popular_products = ""

    context = {
        'product': product,
        'rare_products': rare_products,
        'popular_products': popular_products,
    }

    return render(request, 'products/product_detail.html', context)

