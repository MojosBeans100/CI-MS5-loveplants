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


def ts_and_cs(request):
    """ Return the Terms and Conditions page """

    return render(request, 'home/terms_and_conditions.html')


def privacy_policy(request):
    """ Return the Privacy Policy page """

    return render(request, 'home/privacy_policy.html')


def care(request):
    """ Return the care page """

    return render(request, 'home/care.html')
