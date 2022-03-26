
# Import Django
from django.contrib import admin

# Import local
from .models import Category, Product, PlantCategory


admin.site.register(Category)
admin.site.register(PlantCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'category',
        'plant_category',
        'stock_quantity',
        'price',
        'stock',
        'popular',
    )

    list_filter = ('category', 'stock')