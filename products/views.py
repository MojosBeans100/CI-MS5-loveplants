
# import Django
from django.shortcuts import render, reverse, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from datetime import datetime

# import local
from products.models import (
                    Product,
                    Category,
                    ProductReview,
                    PlantCategory,
                    RecentlyViewed,
                    User)


def all_products(request):
    """
    """

    total_products = Product.objects.filter(stock='in stock')
    all_products = Product.objects.filter(stock='in stock')
    plant_categories = PlantCategory.objects.all()
    search_query = None
    category = None
    stock = None
    plant_cats = None
    sort = None
    direction = None
    current_filters = ""

    if request.GET:

        # copy the dictionary of filters in the front end
        querydict = request.GET.copy()
        print(querydict)

        # for all items in the new request
        for i in request.GET.items():

            print(i)

            # if the filter category is already in the dict
            # change the value
            if i[0] in querydict:
                print("i")
                querydict[i[0]] = i[1]

            # if not, add this filter category
            else:
                querydict.update({i[0]: i[1]})
                print(querydict)
       
        # for i in querydict.items():
        
            current_filters = current_filters + "&" + i[0] + "=" + i[1]
            print(current_filters)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            # if sortkey == 'name':
            #     sortkey == 'lower_name'
            #     all_products = all_products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            all_products = all_products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category']
            category_id = Category.objects.get(name=categories)
            all_products = all_products.filter(category=category_id.id)

        if 'stock' in request.GET:
            all_products = Product.objects.all()
            stock_opt = request.GET['stock'].replace('_', ' ')
            all_products = all_products.filter(stock=stock_opt)

        if 'plant_cats' in request.GET:
            plant_cat = request.GET['plant_cats']
            plant_cat_id = PlantCategory.objects.get(name=plant_cat)
            all_products = all_products.filter(plant_category=plant_cat_id)

        if 'rare' in request.GET:
            all_products = all_products.filter(rare=True)
            
        if 'popular' in request.GET:
            all_products = all_products.filter(popular=True)

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

    current_sorting = f'{sort}_{direction}'
    paginator = Paginator(all_products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_products': all_products,
        'plant_cats': plant_categories,
        'current_sorting': current_sorting,
        'page_obj': page_obj,
        'search_query': search_query,
        'total_products': total_products,
        'current_filters': current_filters,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, id):
    """
    """

    user = str(request.user)
    product = Product.objects.get(id=id)

    if product.rare is True:
        rare_products = Product.objects.filter(rare=True).exclude(id=id)[0:4]
    else:
        rare_products = ""

    if product.popular is True:
        popular_products = Product.objects.filter(popular=True)
        popular_products = popular_products.exclude(id=id)[0:4]
    else:
        popular_products = ""

    if product.care_required == 'low':
        easy_products = Product.objects.filter(care_required='low')
        easy_products = easy_products.exclude(id=id)[0:4]
    else:
        easy_products = ""

    # look for recently viewed products
    product_reviews = ProductReview.objects.filter(product=product.id)

    current_user = User.objects.get(username=user)

    if RecentlyViewed.objects.filter(
                        user=current_user,
                        product=product).exists():
        print("do nothing")
    else:
        viewed_product = RecentlyViewed(
                            user=current_user,
                            viewed=datetime.now(),
                            product=product
                            )
        viewed_product.save()

    recently_viewed = RecentlyViewed.objects.filter(user=current_user)
    recently_viewed_products = []

    for i in recently_viewed:
        product_name = i.product
        recent = Product.objects.get(
                                friendly_name=product_name)
        recently_viewed_product = Product.objects.get(
                                            friendly_name=product_name).name
        # if recent in popular_products or recent in easy_products or recent in rare_products :
        #     print("do nothing")
        # else:
        recently_viewed_products.append(recently_viewed_product)

    recently_viewed = Product.objects.filter(
                                    name__in=recently_viewed_products)[0:4]

    context = {
        'product': product,
        'rare_products': rare_products,
        'popular_products': popular_products,
        'easy_care': easy_products,
        'reviews': product_reviews,
        'recently_viewed': recently_viewed,
    }

    return render(request, 'products/product_detail.html', context)
