# 3rd party imports

# Import Django
from django.contrib import admin

# Import local
from .models import (
                #Category,
                Product,
                #PlantCategory,
                RecentlyViewed,
                ProductReview)


#admin.site.register(Category)
#admin.site.register(PlantCategory)
admin.site.register(RecentlyViewed)


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):

    list_display = (
        'product',
        'user',
        'rating',
        'review_time',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        #'category',
        'plant_category',
        'stock_quantity',
        'price',
        'sale_price',
        'live_on_site',
        'popular',
        'average_rating',
    )

    list_filter = ('plant_category', 'live_on_site')
