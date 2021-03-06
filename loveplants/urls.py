
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('bag/', include('bag.urls')),
    path('products/', include('products.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
]
