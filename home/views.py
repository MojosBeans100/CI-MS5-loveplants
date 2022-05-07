# 3rd party imports

# Django imports
from django.shortcuts import render

# Local imports


def index(request):
    """ Return the homepage """

    return render(request, 'home/index.html')


def error(request):
    """ Return the 404 error page """

    return render(request, 'home/404.html')
