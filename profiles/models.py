# 3rd party imports

# Django imports
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Local imports


class UserProfile(models.Model):
    """
    A class to allow users to create a profile
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )
    default_phone_num = models.CharField(
        max_length=20,
        null=True,
        blank=True
        )
    default_street_address_1 = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    default_street_address_2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    default_town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True
        )
    default_county = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        )
    default_postcode = models.CharField(
        max_length=10,
        null=True,
        blank=True
        )
    default_country = CountryField(
        blank_label='Country *',
        null=True,
        blank=True
        )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Auto create/update user profile upon user creating/updating
    """

    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
