
# import Django
from django.shortcuts import render
from django.db.models import Q

# import local
from products.models import Product, Category


def all_products(request):
    """
    """

    all_products = Product.objects.all()
    search_query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            category_id = Category.objects.get(name=categories)
            all_products = all_products.filter(category=category_id.id)
            print(all_products)

        if 'q' in request.GET:
            search_query = request.GET['q']
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

    # if product.care_required == 'low':
    #     easy_products = Product.objects.filter(care_required='low').exclude(id=id)[0:4]
    # else:
    #     easy_products = ""

    context = {
        'product': product,
        'rare_products': rare_products,
        'popular_products': popular_products,
        #'easy_care': easy_products,
    }

    return render(request, 'products/product_detail.html', context)

