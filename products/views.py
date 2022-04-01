
# import Django
from django.shortcuts import render
from django.db.models import Q

# import local
from products.models import (
                    Product,
                    Category,
                    ProductReview,
                    PlantCategory)


def all_products(request):
    """
    """

    all_products = Product.objects.all()
    plant_categories = PlantCategory.objects.all()
    search_query = None
    category = None
    stock = None
    plant_cats = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            category_id = Category.objects.get(name=categories)
            all_products = all_products.filter(category=category_id.id)

        if 'stock' in request.GET:
            stock_opt = request.GET['stock'].replace('_', ' ')
            all_products = all_products.filter(stock=stock_opt)

        if 'plant_cats' in request.GET:
            plant_cat = request.GET['plant_cats']
            plant_cat_id = PlantCategory.objects.get(name=plant_cat)
            all_products = all_products.filter(plant_category=plant_cat_id)

        if 'price' in request.GET:
            price = request.GET['price'].split(',')
            if len(price) > 1:
                price_low = price[0]
                price_high = price[1]
                all_products = all_products.filter(
                                    price__gte=price_low,
                                    price__lte=price_high
                                    )
            else:
                price_low = price[0]
                all_products = all_products.filter(price__gte=price_low)

        if 'q' in request.GET:
            search_query = request.GET['q']
            search_queries = Q(name__icontains=search_query) | Q(description__icontains=search_query)
            all_products = all_products.filter(search_queries)

    context = {
        'all_products': all_products,
        'plant_cats': plant_categories,
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

    product_reviews = ProductReview.objects.filter(product=product.id)

    context = {
        'product': product,
        'rare_products': rare_products,
        'popular_products': popular_products,
        #'easy_care': easy_products,
        'reviews': product_reviews,
    }

    return render(request, 'products/product_detail.html', context)

