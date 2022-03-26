from django.shortcuts import render
from products.models import Product


def index(request):
    """ Return the homepage """

    return render(request, 'home/index.html')
