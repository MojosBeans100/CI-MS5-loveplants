from django.db import models
from cloudinary.models import CloudinaryField

sun_or_water = (
    ('low', 'low'),
    ('med', 'med'),
    ('high', 'high'),
)

care_demand = (
    ('low', 'low maintenance'),
    ('high', 'high maintenance'),
)

maturity = (
    ('weeks', 'weeks'),
    ('months', 'months'),
    ('years', 'years'),
)


class Category(models.Model):
    """
    A class to define product categories
    """

    name = models.CharField(
        max_length=40
        )

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    A class to define product information
    """

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True
        )
    name = models.CharField(
        max_length=100
        )
    friendly_name = models.CharField(
        max_length=100
        )
    latin_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )
    description = models.TextField()
    description_source = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )
    description_url = models.URLField(
        null=True,
        blank=True
        )
    image_url = CloudinaryField(
        'image',
        default='placeholder'
        )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=6
        )
    stock_quantity = models.PositiveIntegerField(
        null=True,
        blank=True
        )
    pot_size = models.PositiveIntegerField(
        null=True,
        blank=True
        )
    height = models.PositiveIntegerField(
        null=True,
        blank=True
        )
    length = models.PositiveIntegerField(
        null=True,
        blank=True
        )
    maturity_num = models.PositiveIntegerField(
        null=True,
        blank=True
        )
    maturity_time = models.CharField(
        choices=maturity,
        max_length=15,
        null=True,
        blank=True
        )
    sunlight = models.CharField(
        choices=sun_or_water,
        max_length=15,
        null=True,
        blank=True
        )
    watering = models.CharField(
        choices=sun_or_water,
        max_length=15,
        null=True,
        blank=True
        )
    care_required = models.BooleanField(
        choices=care_demand,
        null=True,
        blank=True
        )
    rare = models.BooleanField(
        null=True,
        blank=True
        )
    popular = models.BooleanField(
        null=True,
        blank=True
        )
    out_of_stock = models.BooleanField(
        null=True,
        blank=True
        )
    returning_soon = models.BooleanField(
        null=True,
        blank=True
        )

    class Meta:
        ordering = ['-stock_quantity']

    def __str__(self):
        return self.friendly_name
