
# 3rd party imports
from slugify import slugify
import decimal
import json

# Django imports
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.db.models import Q, Max
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Local imports
from products.models import (
                    Product,
                    ProductReview,
                    )
from .forms import ProductReviewForm, ProductForm
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem


def all_products(request):
    """
    Display all products to the user, allowing for
    filtering and sorting
    """
    #messages.error(request, "This item could not be added to your basket at this time.")
    messages.error(request, "This item was successfully added to your basket.")
    # all_products = Product.objects.all()
    # for i in all_products:
    #     i.average_rating = 0
    #     i.save()

    if request.user.is_superuser:
        all_products = Product.objects.all()
    else:
        all_products = Product.objects.filter(live_on_site=True)

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

        # for all items in the new request
        for i in request.GET.items():

            # if the filter category is already in the dict
            # change the value
            if i[0] in querydict:
                querydict[i[0]] = i[1]

            # if not, add this filter category
            else:
                querydict.update({i[0]: i[1]})

            # # if the filter category says remove
            # # remove it
            # if i[0] == 'remove':
            #     querydict.pop('remove')
            #     querydict.pop(i[1])

        for j in querydict.items():
            current_filters = current_filters + "&" + j[0] + "=" + j[1]

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                    print(sortkey)
            all_products = all_products.order_by(sortkey)

        if 'plant_cats' in request.GET:
            plant_cat = request.GET['plant_cats']
            all_products = all_products.filter(plant_category=plant_cat)
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

        if 'easycare' in request.GET:
            all_products = all_products.filter(
                care_required='can stand a little neglect')

        # sale price
        if 'price' in request.GET:
            price = request.GET['price'].split(',')
            if len(price) > 1:
                price_low = price[0]
                price_high = price[1]
                all_products = all_products.filter(
                                    price__gte=price_low,
                                    price__lte=price_high
                                    )
                filtered_by = ['price',
                               f'{price_low}-{price_high}',
                               f'£{price_low} - £{price_high}']
            else:
                price_low = price[0]
                all_products = all_products.filter(price__gte=price_low)
                filtered_by = ['price',
                               f'{price_low}',
                               f'£{price_low}+']

            front_end_filters.append(filtered_by)

        if 'q' in request.GET:
            search_query = request.GET['q']
            search_queries = (
                              Q(name__icontains=search_query)
                              | Q(description__icontains=search_query)
                              | Q(latin_name__icontains=search_query)
                            )
            all_products = all_products.filter(search_queries)

        if 'liveonsite' in request.GET:
            all_products = all_products.filter(live_on_site=True)

    current_sorting = f'{sort}_{direction}'
    paginator = Paginator(all_products, 16)
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
        'current_sorting': current_sorting,
        'page_obj': page_obj,
        'search_query': search_query,
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

    liked = None
    has_purchased = None
    already_reviewed = None
    form = None
    purchase_date = None

    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return render(request, 'home/404.html')

    product_reviews = ProductReview.objects.filter(product=product.id)
    product_reviews = product_reviews.exclude(review="")

    if product.rare is True:
        rare_products = Product.objects.filter(rare=True).exclude(id=id)
        rare_products = rare_products.filter(live_on_site=True)[0:4]
    else:
        rare_products = None

    if product.popular is True:
        popular_products = Product.objects.filter(popular=True)
        popular_products = popular_products.filter(live_on_site=True)
        popular_products = popular_products.exclude(id=id)[0:4]
    else:
        popular_products = None

    if product.care_required == 'low':
        easy_products = Product.objects.filter(care_required='low')
        easy_products = easy_products.filter(live_on_site=True)
        easy_products = easy_products.exclude(id=id)[0:4]
    else:
        easy_products = None

    if (rare_products is None
            and popular_products is None
            and easy_products is None):
        more_products = Product.objects.filter(live_on_site=True)
        more_products = more_products.exclude(id=id)[0:4]
    else:
        more_products = None

    if request.user.is_authenticated:

        try:
            liked_product = ProductReview.objects.get(
                product=product.id, user=request.user)
            liked = liked_product.liked
        except:
            liked = None

        has_purchased = False
        already_reviewed = False
        user_profile = UserProfile.objects.get(user=request.user)
        users_orders = Order.objects.filter(user_profile=user_profile)

        for order in users_orders:
            line_item = OrderLineItem.objects.filter(product=product)
            for item in line_item:
                if item.order.order_ref == order.order_ref:
                    has_purchased = True
                    purchase_date = order.date

        try:
            users_reviews = ProductReview.objects.get(
                product=product,
                user=request.user)
            if users_reviews.review != "":
                already_reviewed = True
        except:
            already_reviewed = False

        if has_purchased is True and already_reviewed is not True:
            form = ProductReviewForm(initial={
                'product': product.friendly_name,
            })
        else:
            form = None

    context = {
        'product': product,
        'rare_products': rare_products,
        'popular_products': popular_products,
        'easy_care': easy_products,
        'reviews': product_reviews,
        'has_purchased': has_purchased,
        'purchase_date': purchase_date,
        'already_reviewed': already_reviewed,
        'form': form,
        'liked': liked,
        'more_products': more_products,
    }

    return render(request, 'products/product_detail.html', context)


def product_like(request, id):
    """
    Allows users to like or unlike products
    """

    try:
        product = Product.objects.get(pk=id)
        if request.method == 'POST':
            if ProductReview.objects.filter(product=product,
                                            user=request.user).exists():
                product_review = ProductReview.objects.get(
                                                        product=product,
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
                print(product_review.rating)

    except Product.DoesNotExist:
        return render(request, 'home/404.html')

    redirect_url = request.POST.get('redirect_url',
                                    '/products/products.html')
    return redirect((redirect_url))


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
        reviewed_product.save()

    redirect_url = request.POST.get('redirect_url')

    return redirect(redirect_url)


def admin_add_product(request):
    """
    Allow an admin user to add a product
    """

    form = ProductForm()
    error_fields = []
    error_messages = []

    if request.user.is_superuser:

        if request.method == 'POST':
            #print(request.POST)

            if 'popular' in request.POST:
                popular = True
            else:
                popular = False

            if 'rare' in request.POST:
                rare = True
            else:
                rare = False

            if 'live_on_site' in request.POST:
                live_on_site = True
            else: 
                live_on_site = False

            x = request.POST['care_instructions_source']
            form_data = {
                'plant_category': request.POST['plant_category'],
                'name': slugify(request.POST['friendly_name'], separator='_'),
                'friendly_name': request.POST['friendly_name'],
                'latin_name': request.POST['latin_name'],
                'description': request.POST['description'],
                'description_source': request.POST['description_source'],
                'description_url': request.POST['description_url'],
                'image1_source': request.POST['image1_source'],
                'image1_source_url': request.POST['image1_source_url'],
                'image2_source': request.POST['image2_source'],
                'image2_source_url': request.POST['image2_source_url'],
                'image3_source': request.POST['image3_source'],
                'image3_source_url': request.POST['image3_source_url'],
                'pot_size': request.POST['pot_size'],
                'height': request.POST['height'],
                'price': request.POST['price'],
                'stock_quantity': request.POST['stock_quantity'],
                'maturity_num': request.POST['maturity_num'],
                'maturity_time': request.POST['maturity_time'],
                'sunlight': request.POST['sunlight'],
                'watering': request.POST['watering'],
                'care_required': request.POST['care_required'],
                'care_instructions': request.POST['care_instructions'],
                'care_instructions_source': x,
                'care_instructions_url': request.POST['care_instructions_url'],
                'rare': rare,
                'popular': popular,
                'live_on_site': live_on_site,
                'average_rating': 0,
            }
            form = ProductForm(form_data)

            if form.is_valid:
                if form.errors:
                    print(form.errors.as_json())
                    errors = json.loads(form.errors.as_json())
                    keys = list(errors.keys())
                    values = list(errors.values())

                    for i in keys:
                        error_fields.append(i)

                    for i in values:
                        error_messages.append(i[0]['message'])

                    messages.error(
                                request,
                                "The product could not be"
                                " added at this time."
                                " Please refer to the list of errors."
                                )
                    errors = form.errors.as_json()
                    form = ProductForm(form_data)

                else:
                    form.save()
                    latestid = Product.objects.aggregate(
                            Max('id'))['id__max']
                    latest_product = Product.objects.get(id=latestid)
                    messages.success(
                        request,
                        f"'{latest_product.friendly_name}' "
                        "successfully added."
                        " This product is live on the site"
                        " and available to purchase."
                        )
                    return redirect(reverse(
                                    'product_detail',
                                    args=[latestid]))

        saved_products = Product.objects.filter(live_on_site=False)[0:4]
        context = {
            'form': form,
            'saved': saved_products,
            'error_fields': error_fields,
            'error_messages': error_messages,
        }

    else:
        messages.error(
            request,
            "Only admin users are allowed to access that page. ")
        return render(request, 'home/404.html')

    return render(request, 'products/add_product.html', context)


def admin_edit_product(request, id):
    """
    Allow admin users to edit product details
    or create a new object with similar fields
    """

    if request.user.is_superuser:
        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return render(request, 'home/404.html')
            
        form = ProductForm(instance=product)

        if request.method == 'POST':
            valid_array = []
            for i in request.POST:
                if request.POST[i] == "" and i != 'save-as-new':
                    valid_array.append('false')

            # check this
            if 'popular' in request.POST:
                popular = True
            else:
                popular = False

            if 'rare' in request.POST:
                rare = True
            else:
                rare = False

            if 'save-as-new' in request.POST:

                try:
                    x = request.POST['friendly_name']
                    Product.objects.get(
                        friendly_name=x)
                    messages.error(
                        request, (f"'{x}' "
                                  "already exists:"
                                  " the name of the plant "
                                  "must be unique."))
                    return redirect(reverse('edit_product', args=[id]))

                except Product.DoesNotExist:
                    if 'live_on_site' in request.POST:
                        if len(valid_array) > 0:
                            messages.error(
                                request,
                                ('Cannot add product to'
                                 ' live website due to'
                                 ' empty fields.'
                                 ' Fill in entire'
                                 ' form or uncheck '
                                 '"live on site"'))
                            return redirect(reverse('edit_product', args=[id]))

                    x = request.POST['friendly_name']
                    des = request.POST['description_source']
                    care_source = request.POST['care_instructions_source']
                    care_url = request.POST['care_instructions_url']

                    form_data = {
                        #'category': request.POST['category'],
                        'plant_category': request.POST['plant_category'],
                        'name': slugify(x, separator='_'),
                        'friendly_name': request.POST['friendly_name'],
                        'latin_name': request.POST['latin_name'],
                        'description': request.POST['description'],
                        'description_source': des,
                        'description_url': request.POST['description_url'],
                        #'image1_source': request.POST['image1_source'],
                        'image1_source_url': request.POST['image1_source_url'],
                        #'image2_source': request.POST['image2_source'],
                        'image2_source_url': request.POST['image2_source_url'],
                        #'image3_source': request.POST['image3_source'],
                        'image3_source_url': request.POST['image3_source_url'],
                        'pot_size': request.POST['pot_size'],
                        'height': request.POST['height'],
                        'price': request.POST['price'],
                        #'length': request.POST['length'],
                        'stock_quantity': request.POST['stock_quantity'],
                        'maturity_num': request.POST['maturity_num'],
                        'maturity_time': request.POST['maturity_time'],
                        'sunlight': request.POST['sunlight'],
                        'watering': request.POST['watering'],
                        'care_required': request.POST['care_required'],
                        'care_instructions': request.POST['care_instructions'],
                        'care_instructions_source': care_source,
                        'care_instructions_url': care_url,
                        'rare': rare,
                        'popular': popular,
                        'average_rating': 0,
                    }
                    form = ProductForm(form_data)
                    if form.is_valid:
                        form.save()
                        x = (f"{request.POST['friendly_name']}"
                             " has been created")
                        messages.success(request, x)
                        latestid = Product.objects.aggregate(
                            Max('id'))['id__max']
                        return redirect(reverse(
                            'product_detail',
                            args=[latestid]))
                    else:
                        print("errors")

                return redirect(reverse('products'))

            else:
                form = ProductForm(request.POST, instance=product)

                if 'live_on_site' in request.POST:
                    if len(valid_array) > 0:
                        messages.success(
                            request,
                             ('Cannot add product to'
                              ' live website due to'
                              ' empty'
                              ' fields.  Fill in entire'
                              ' form or uncheck '
                              '"live on site"'))
                        return redirect(reverse('edit_product', args=[id]))

                if form.is_valid():
                    form.save()
                    x = (f"{request.POST['friendly_name']}"
                         " has been edited.")
                    messages.success(request, x)
                else:
                    print(form.errors)
                    print("errors")

                return redirect(reverse('product_detail', args=[id]))

        context = {
            'form': form,
            'product': product,
        }

    else:
        messages.error(
            request,
            "Only admin users are allowed to access that page. ")
        return render(request, 'home/404.html')

    return render(request, 'products/edit_product.html', context)


def admin_delete_product(request, id):
    """
    Allow admin users to delete products
    """

    if request.user.is_superuser:

        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return render(request, 'home/404.html')

        try:
            product.delete()
            messages.success(
                request,
                f"{product.friendly_name} has been deleted."
                )
        except:
            messages.error(
                request,
                "Error: this product could not be deleted."
                "  Please try again later. ")
    else:
        return render(request, 'home/404.html')

    return redirect(reverse('products'))


def admin_create_sale(request):

    if request.user.is_superuser:
        all_products = Product.objects.filter(
                                        sale_price=None
                                        ).order_by(
                                            'plant_category')
        sale_products = Product.objects.filter(
            sale_price__gte=0).order_by(
                                            'plant_category')

        if request.method == 'POST':

            if 'apply-sale' in request.POST:
                per = None
                val = None
                if (request.POST['val']) != "":
                    val = decimal.Decimal(request.POST['val'])
                if (request.POST['per']) != "":
                    per = decimal.Decimal(request.POST['per'])

                for product in all_products:
                    try:
                        product_id = request.POST[f"{product.id}"]
                        change_price = Product.objects.get(id=product_id)
                        if val is None and per is not None:
                            change_price.sale_price = round(
                                ((100-per)/100)*change_price.price, 2
                                )
                        else:
                            change_price.sale_price = change_price.price - val
                        change_price.save()
                        all_products = Product.objects.filter(sale_price=None)
                        sale_products = Product.objects.filter(
                                                        sale_price__gte=0
                                                        )
                        messages.success(request, "Items added to sale")
                    except:
                        ...

            else:
                for product in sale_products:
                    try:
                        product_id = request.POST[f"{product.id}"]
                        remove_sale_price = Product.objects.get(id=product_id)
                        remove_sale_price.sale_price = None
                        remove_sale_price.save()
                        all_products = Product.objects.filter(sale_price=None)
                        sale_products = Product.objects.filter(
                                                        sale_price__gte=0
                                                        )
                        messages.success(request, "Items removedfrom sale")
                    except:
                        ...

        context = {
            'products': all_products,
            'sale_products': sale_products,
        }

    else:
        return render(request, 'home/404.html')

    return render(request, 'products/create_sale.html', context)
