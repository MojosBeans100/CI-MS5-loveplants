from django.shortcuts import render


def index(request):
    """ Return the homepage """

    return render(request, 'home/index.html')
