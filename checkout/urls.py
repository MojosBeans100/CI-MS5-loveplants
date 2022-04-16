
# 3rd party imports

# Django imports
from django.urls import path

# Local imports
from . import views
from .webhooks import webhook

urlpatterns = [
    path('checkout.html',
         views.view_checkout,
         name='view_checkout'),
    path('checkout_success/<order_ref>',
         views.checkout_success,
         name='checkout_success'),
     path('wh/', webhook, name='webhook'),
]
