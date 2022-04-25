
# 3rd party imports

# Django imports
from django.urls import path

# Local imports
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('edit/<item_id>/', views.edit_bag, name='edit_bag'),
    path('delete/<item_id>/', views.delete_bag, name='delete_bag'),
]
