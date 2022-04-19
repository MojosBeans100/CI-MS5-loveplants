# 3rd party imports

# Django imports
from django.contrib import admin

# Local imports
from .models import UserProfile, User

admin.site.register(UserProfile)
