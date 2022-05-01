
# 3rd party imports
from slugify import slugify
import decimal

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

        # if 'category' in request.GET:
        #     categories = request.GET['category']
        #     category_id = Category.objects.get(name=categories)
        #     all_products = all_products.filter(category=category_id.id)

        # if 'stock' in request.GET:
        #     all_products = Product.objects.all()
        #     stock_opt = request.GET['stock'].replace('_', ' ')
        #     all_products = all_products.filter(stock=stock_opt)
        #     filtered_by = stock_opt

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
        #'plant_cats': plant_categories,
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

    has_purchased = None
    already_reviewed = None
    form = None
    purchase_date = None
    product = get_object_or_404(Product, pk=id)
    print(product.name)
    print(product.average_rating)
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

        try:
            liked_product = ProductReview.objects.get(
                product=product.id, user=request.user)
            liked = liked_product.liked
        except:
            liked = None

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

        # current_user = User.objects.get(username=user)
        # if RecentlyViewed.objects.filter(
        #                     user=current_user,
        #                     product=product).exists():
        #     print("do nothing")
        # else:
        #     viewed_product = RecentlyViewed(
        #                         user=current_user,
        #                         viewed=datetime.now(timezone.utc),
        #                         product=product
        #                         )
        #     viewed_product.save()

        # recently_viewed = RecentlyViewed.objects.filter(user=current_user)
        # recently_viewed_products = []

        # for i in recently_viewed:
        #     product_name = i.product
        #     recently_viewed_product = Product.objects.get(
        #                                     friendly_name=product_name).name
        #     recently_viewed_products.append(recently_viewed_product)

        # recently_viewed = Product.objects.filter(
        #                                 name__in=recently_viewed_products)[0:4]
  
    context = {
        'product': product,
        'rare_products': rare_products,
        'popular_products': popular_products,
        'easy_care': easy_products,
        'reviews': product_reviews,
        # 'recently_viewed': recently_viewed,
        'has_purchased': has_purchased,
        'purchase_date': purchase_date,
        'already_reviewed': already_reviewed,
        'form': form,
        'liked': liked,
    }

    return render(request, 'products/product_detail.html', context)


def product_like(request, id):
    """
    Allows users to like or unlike products
    """

    if request.method == 'POST':

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
        reviewed_product.save()

    redirect_url = request.POST.get('redirect_url')

    return redirect(redirect_url)


def admin_add_product(request):
    """
    Allow an admin user to add a product
    """

    if request.method == 'POST':

        if 'popular' in request.POST:
            popular = True
        else:
            popular = False

        if 'rare' in request.POST:
            rare = True
        else:
            rare = False

        # save the object
        if 'save-form' in request.POST:

            form = ProductForm(request.POST)
            if form.is_valid:
                form.save()
            return redirect(reverse('products'))

        # post the object
        else:
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
                'live_on_site': True,
                'average_rating': 0,
            }

            form = ProductForm(form_data)
            if form.is_valid:
                form.save()

            return redirect(reverse('products'))

    form = ProductForm()
    saved_products = Product.objects.filter(live_on_site=False)
    context = {
        'form': form,
        'saved': saved_products,
    }

    return render(request, 'products/add_product.html', context)


def admin_edit_product(request, id):
    """
    Allow admin users to edit product details
    or create a new object with similar fields
    """

    if request.user.is_superuser:
        product = Product.objects.get(id=id)
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
                    messages.success(request, (f"{x} "
                                               "already exists:"
                                               " the name of the plant "
                                               "must be unique."))
                    return redirect(reverse('edit_product', args=[id]))
                except Product.DoesNotExist:

                    if 'live_on_site' in request.POST:
                        if len(valid_array) > 0:
                            messages.success(request, ('Cannot add product to'
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
                        messages.success(request, ('Cannot add product to'
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
                    print("errors")

                return redirect(reverse('product_detail', args=[id]))

        context = {
            'form': form,
            'product': product,
        }

    else:
        return render('product/products.html')

    return render(request, 'products/edit_product.html', context)


def admin_delete_product(request, id):
    """
    Allow admin users to delete products
    """

    if request.user.is_superuser:
        product = Product.objects.get(id=id)
        product.delete()
        messages.success(request, f"{product.friendly_name} has been deleted.")
    else:
        return render('product/products.html')

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

                    product_id = request.POST[f"{product.id}"]

                    try:
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
                    except:
                        ...

        context = {
            'products': all_products,
            'sale_products': sale_products,
        }

    else:
        return render('product/products.html')

    return render(request, 'products/create_sale.html', context)
