# 3rd party imports

# Django imports
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Local imports


class UserProfile(models.Model):
    """
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )
    default_phone_num = models.CharField(
        max_length=20,
        null=False,
        blank=True
        )
    default_country = CountryField(
        blank_label='Country *',
        null=False,
        blank=True
        )
    default_postcode = models.CharField(
        max_length=10,
        null=False,
        blank=True
        )
    default_town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=True
        )
    default_street_address_1 = models.CharField(
        max_length=80,
        null=False,
        blank=True
        )
    default_street_address_2 = models.CharField(
        max_length=80,
        null=False,
        blank=True
        )
    default_county = models.CharField(
        max_length=80,
        null=False,
        blank=True,
    )
