# 3rd party imports

# Django imports
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Local imports
from products.models import (
                    Product,
                    ProductReview
                    )
from checkout.models import (
                    OrderLineItem
                    )
from .models import UserProfile, User
from .forms import UserProfileForm


def profile(request):
    """
    Display the user's profile page, default delivery info,
    order history
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    user_profile = get_object_or_404(User, username=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated profile details.")

    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.filter(user_profile=profile).order_by('-date')
    line_items = OrderLineItem.objects.all()

    context = {
        'form': form,
        'orders': orders,
        'line_items': line_items,
        'user_profile': user_profile,
    }

    return render(request, 'profiles/profile.html', context)


def liked_products(request):
    """
    Display products liked by the user
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
