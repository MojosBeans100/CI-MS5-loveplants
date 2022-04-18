# 3rd party imports
# Django imports
from django.shortcuts import render

# Local imports


def profile(request):
    """
    """
    context = {}

    return render(request, 'profiles/profile.html', context)