
# Import Django
from django.contrib import admin

# Import local
from .models import Category, Product, PlantCategory


admin.site.register(Category)
admin.site.register(PlantCategory)
admin.site.register(Product)