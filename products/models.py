from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

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

stock_options = (
    ('in stock', 'In stock'),
    ('out of stock', 'Out of stock'),
    ('returning soon', 'Returning soon'),
)

rating = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class Category(models.Model):
    """
    A class to define product categories
    """

    name = models.CharField(
        max_length=40
        )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class PlantCategory(models.Model):
    """
    A class to define plant categories
    """
    name = models.CharField(
        max_length=50
    )

    class Meta:
        verbose_name_plural = 'Plant Categories'

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
    plant_category = models.ForeignKey(
        'PlantCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
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
    image1_source = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    image1_source_url = models.URLField(
        max_length=400,
        null=True,
        blank=True
    )
    image2_source = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    image2_source_url = models.URLField(
        max_length=400,
        null=True,
        blank=True
    )
    image3_source = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    image3_source_url = models.URLField(
        max_length=400,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        verbose_name='Price (£)'
        )
    stock_quantity = models.PositiveIntegerField(
        null=True,
        blank=True
        )
    pot_size = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Pot size (cm)'
        )
    height = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Height (cm)'
        )
    length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Length (cm)'
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
    care_required = models.CharField(
        choices=care_demand,
        max_length=50,
        null=True,
        blank=True
        )
    care_instructions = models.TextField(
        null=True,
        blank=True
    )
    care_instructions_source = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    care_instructions_url = models.URLField(
        max_length=400,
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
    stock = models.CharField(
        choices=stock_options,
        max_length=100,
        default='out of stock'
    )

    class Meta:
        ordering = ['-stock_quantity']

    def __str__(self):
        return self.friendly_name


class RecentlyViewed(models.Model):
    """
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
        )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )

    viewed = models.DateTimeField()


class ProductReview(models.Model):
    """
    """
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
        )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
        )

    review = models.TextField(
        max_length=250,
        null=False,
        blank=False
        )

    rating = models.IntegerField(
        choices=rating,
        default=5
        )
