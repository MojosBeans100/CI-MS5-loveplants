
# import Django
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime

# import local
from products.models import (
                    Product,
                    Category,
                    ProductReview,
                    PlantCategory,
                    RecentlyViewed,
                    User)
from .forms import ProductReviewForm
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem

def all_products(request):
    """
    Display all products to the user, allowing for
    filtering and sorting
    """

    total_products = Product.objects.filter(stock='in stock')
    all_products = Product.objects.filter(stock='in stock')
    plant_categories = PlantCategory.objects.all()
    search_query = None
    sort = None
    direction = None
    current_filters = ""
    querydict = ""
    front_end_filters = []
    filtered_by = ""

    if request.GET:

        # copy the dictionary of filters in the front end
        querydict = request.GET.copy()
        # myDict = dict(request.GET.lists())

        # for all items in the new request
        for i in request.GET.items():

            # if the filter category is already in the dict
            # change the value
            if i[0] in querydict:

                querydict[i[0]] = i[1]

            # if not, add this filter category
            else:
                querydict.update({i[0]: i[1]})

            # if the filter category says remove
            # remove it
            if i[0] == 'remove':
                querydict.pop('remove')
                querydict.pop(i[1])

        for j in querydict.items():
            current_filters = current_filters + "&" + j[0] + "=" + j[1]

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

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
            filtered_by = stock_opt

        if 'plant_cats' in request.GET:
            plant_cat = request.GET['plant_cats']
            plant_cat_id = PlantCategory.objects.get(name=plant_cat)
            all_products = all_products.filter(plant_category=plant_cat_id)
            filtered_by = ['plant_cats', plant_cat, f'{plant_cat} plants']
            front_end_filters.append(filtered_by)

        if 'sunlight' in request.GET:
            sunlight = request.GET['sunlight']
            all_products = all_products.filter(sunlight=sunlight)
            filtered_by = ['sunlight', sunlight, f'{sunlight}']
            front_end_filters.append(filtered_by)

        if 'watering' in request.GET:
            watering = request.GET['watering']
            all_products = all_products.filter(watering=watering)
            filtered_by = ['watering', watering, f'{watering}']
            front_end_filters.append(filtered_by)

        if 'rare' in request.GET:
            all_products = all_products.filter(rare=True)
            filtered_by = "Rare"
            front_end_filters.append(filtered_by)

        if 'popular' in request.GET:
            all_products = all_products.filter(popular=True)
            filtered_by = "Popular"
            front_end_filters.append(filtered_by)

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
            filtered_by = ['price',
                           f'{price_low}-{price_high}',
                           f'£{price_low} - £{price_high}']
            front_end_filters.append(filtered_by)

        if 'q' in request.GET:
            search_query = request.GET['q']
            # check this still works with line broken up
            search_queries = Q(name__icontains=search_query) \
                | Q(description__icontains=search_query)
            all_products = all_products.filter(search_queries)

    current_sorting = f'{sort}_{direction}'
    paginator = Paginator(all_products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    liked_products_list = []

    if request.user.is_authenticated:
        liked_products = ProductReview.objects.filter(user=request.user,
                                                      liked=True)
        for i in liked_products:
            liked_products_list.append(i.product.friendly_name)

    context = {
        'all_products': all_products,
        'plant_cats': plant_categories,
        'current_sorting': current_sorting,
        'page_obj': page_obj,
        'search_query': search_query,
        'total_products': total_products,
        'current_filters': current_filters,
        'filtered_by': filtered_by,
        'front_end_filters': front_end_filters,
        'liked_list': liked_products_list,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, id):
    """
    Display details about a product
    """

    user = str(request.user)
    product = Product.objects.get(id=id)
    recently_viewed = ""
    product_reviews = ProductReview.objects.filter(product=product.id)

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
    if request.user.is_authenticated:

        # product review
        has_purchased = False
        already_reviewed = False
        user_profile = UserProfile.objects.get(user=request.user)
        users_orders = Order.objects.filter(user_profile=user_profile)

        for order in users_orders:
            line_item = OrderLineItem.objects.filter(product=product)
            for item in line_item:
                if item.order.order_ref == order.order_ref:
                    has_purchased = True

        users_reviews = ProductReview.objects.filter(product=product, user=request.user)
        if len(users_reviews) != 0:
            already_reviewed = True

        if has_purchased is True and already_reviewed is not True:
            form = ProductReviewForm(initial={
                'product': product.friendly_name,
            })
        else:
            form = ""

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
            recently_viewed_product = Product.objects.get(
                                            friendly_name=product_name).name
            recently_viewed_products.append(recently_viewed_product)

        recently_viewed = Product.objects.filter(
                                        name__in=recently_viewed_products)[0:4]

    # calculate average product rating
    num_reviews = ProductReview.objects.filter(product=product).count()
    ratings = []
    count = 0
    sum = 0
    if num_reviews != 0:
        for review in product_reviews:
            ratings.append(review.rating)
            sum += review.rating
            count += 1
        average_rating = sum/count
        product.average_rating = average_rating
        product.save()

    context = {
        'product': product,
        'rare_products': rare_products,
        'popular_products': popular_products,
        'easy_care': easy_products,
        'reviews': product_reviews,
        'recently_viewed': recently_viewed,
        'has_purchased': has_purchased,
        'already_reviewed': already_reviewed,
        'form': form,
        'num_reviews': num_reviews,
    }

    return render(request, 'products/product_detail.html', context)


def product_like(request, id):
    """
    Allows users to like or unlike products
    """

    product = Product.objects.get(id=id)
    if ProductReview.objects.filter(product=product,
                                    user=request.user).exists():
        product_review = ProductReview.objects.get(product=product,
                                                   user=request.user)
        if product_review.liked is True:
            product_review.liked = False
            product_review.save()
        else:
            product_review.liked = True
            product_review.save()
    else:
        product_review = ProductReview(product=product,
                                       user=request.user,
                                       liked=True)
        product_review.save()

    redirect_url = request.POST.get('redirect_url')

    return redirect(redirect_url)


def product_review(request, id):
    """
    Allow users to add review or rating to a product
    if they have previously purchased it
    """

    if request.method == 'POST':
        form_data = {
            'review': request.POST['review'],
            'rating': request.POST['rating'],
            'product': Product.objects.get(id=id)
        }

        review_form = ProductReviewForm(form_data)
        if review_form.is_valid:
            review_form.save()

        reviewed_product = ProductReview.objects.latest()
        reviewed_product.user = request.user
        reviewed_product.review_time = datetime.now()
        reviewed_product.save()

    redirect_url = request.POST.get('redirect_url')

    return redirect(redirect_url)
