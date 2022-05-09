# 3rd party imports
from slugify import slugify

# Django imports
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from datetime import datetime, timezone

# Local imports

plant_cats = (
    ('Potted', 'potted'),
    ('Hanging', 'hanging'),
    ('Floor', 'floor'),
    ('Flowers', 'flowers'),
    ('Succulents', 'succulents'),
)

sun_or_water = (
    ('low', 'low'),
    ('med', 'med'),
    ('high', 'high'),
)

care_demand = (
    ('can stand a little neglect', 'low maintenance'),
    ('requires frequent care', 'high maintenance'),
)

maturity = (
    ('weeks', 'weeks'),
    ('months', 'months'),
    ('years', 'years'),
)

rating = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Product(models.Model):
    """
    A class to define product information
    """

    plant_category = models.CharField(
        choices=plant_cats,
        max_length=30,
        null=True,
        blank=True,
        default=None,
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        editable=False,
        )
    friendly_name = models.CharField(
        max_length=100,
        unique=True
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
    sale_price = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        verbose_name='Sale Price (£)',
        blank=True,
        null=True
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
        default=False,
        null=True,
        )
    popular = models.BooleanField(
        default=False,
        null=True,
        )
    live_on_site = models.BooleanField(
        default=False,
    )
    average_rating = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-stock_quantity']

    def __str__(self):
        return self.friendly_name

    def save(self, *args, **kwargs):
        """
        Override original save method to add the name based on
        friendly name
        """

        if not self.name:
            self.name = slugify(self.friendly_name, separator='_')
        super().save(*args, **kwargs)


class RecentlyViewed(models.Model):
    """
    A models to allow users to see what they've recently viewed
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
    A model to allow users to leave a review for a product
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
    review_time = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    review_time_ago = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    liked = models.BooleanField(
        default=False,
    )

    class Meta:
        get_latest_by = 'id'

    def save(self, *args, **kwargs):
        """
        Override original save method to calc review time ago
        """
        self.review_time = datetime.now(timezone.utc)
        self.review_time_ago = ((datetime.now(timezone.utc)
                                - self.review_time).days)
        super().save(*args, **kwargs)


@receiver(post_save, sender=ProductReview)
def update_average_rating(sender, instance, created, **kwargs):
    """
    Update product average rating each time a new rating is added
    """

    product = Product.objects.get(pk=instance.product.pk)
    product_reviews = ProductReview.objects.filter(product=product.id)
    num_reviews = ProductReview.objects.filter(
        product=instance.product.id).count()
    ratings = []
    count = 0
    sum = 0
    if num_reviews != 0:
        for review in product_reviews:
            ratings.append(review.rating)
            sum += review.rating
            count += 1
        average_rating = sum/count
        product.average_rating = average_rating
        product.save()
    else:
        product.average_rating = 5


@receiver(post_delete, sender=ProductReview)
def update_average_rating_deleted(sender, instance, **kwargs):
    """
    Update average rating on deletion of a review
    """
    product = Product.objects.get(pk=instance.product.pk)
    product_reviews = ProductReview.objects.filter(product=product.id)
    num_reviews = ProductReview.objects.filter(
        product=instance.product.id).count()
    ratings = []
    count = 0
    sum = 0
    if num_reviews != 0:
        for review in product_reviews:
            ratings.append(review.rating)
            sum += review.rating
            count += 1
        average_rating = sum/count
        product.average_rating = average_rating
        product.save()
    else:
        product.average_rating = 5
