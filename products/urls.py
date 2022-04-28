# 3rd party imports

# Django imports
from django.urls import path

# Local imports
from . import views

urlpatterns = [
    path('products.html',
         views.all_products,
         name='products'),
    path('add_product.html',
         views.admin_add_product,
         name='add_product'),
#     path('delete_product/<int:id>',
#          views.admin_delete_product,
#          name='delete_product'),
    path('edit_product/<int:id>',
         views.admin_edit_product,
         name='edit_product'),
    path('product_detail/<int:id>',
         views.product_detail,
         name='product_detail'),
    path('product_like/<int:id>',
         views.product_like,
         name='product_like'),
    path('product_review/<int:id>',
         views.product_review,
         name='product_review'),
    path('create_sale.html',
         views.admin_create_sale,
         name='create_sale'),
]
