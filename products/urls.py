from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products.html', views.all_products, name='products'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
]
