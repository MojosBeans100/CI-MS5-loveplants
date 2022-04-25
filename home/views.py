# 3rd party imports

# Django imports
from django.shortcuts import render

# Local imports


def index(request):
    """ Return the homepage """

    return render(request, 'home/index.html')
