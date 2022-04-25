
# 3rd party imports

# Django imports
from django.urls import path

# Local imports
from . import views

urlpatterns = [
    path('', views.index, name='home')
]
