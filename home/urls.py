
# 3rd party imports

# Django imports
from django.urls import path

# Local imports
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('404.html', views.error, name="404"),
    path('terms_and_conditions.html', views.ts_and_cs, name="ts_and_cs"),
    path('privacy_policy.html', views.privacy_policy, name="privacy_policy")
]
