
# 3rd party imports

# Django imports
from django.urls import path

# Local imports
from . import views

urlpatterns = [
    path('checkout.html', views.view_checkout, name='view_checkout'),
]
