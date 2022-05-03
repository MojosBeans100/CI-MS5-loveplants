# 3rd party imports
import uuid
import decimal

# Django imports
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

# Local imports
from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    A model for each time a user places an order
    """

    order_ref = models.CharField(
        max_length=32,
        null=False,
        editable=False
        )
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
        )
    full_name = models.CharField(
        max_length=60,
        null=False,
        blank=False
        )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
        )
    phone_num = models.CharField(
        max_length=20,
        null=False,
        blank=False
        )
    street_address_1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
        )
    street_address_2 = models.CharField(
        max_length=80,
        null=False,
        blank=True
        )
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
        )
    county = models.CharField(
        max_length=80,
        null=False,
        blank=True,
    )
    postcode = models.CharField(
        max_length=10,
        null=False,
        blank=True
        )
    country = CountryField(
        blank_label='Country *',
        null=False,
        blank=False
        )

    date = models.DateTimeField(
        auto_now=True
        )
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        null=False
        )
    order_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        null=False
        )
    grand_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        null=False
        )
    original_bag = models.TextField(
        null=False,
        blank=False,
        default=''
        )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default='')

    def update_total(self):
        """
        Update the grand total when a line item is added
        and calc delivery costs
        """

        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = decimal.Decimal(8.99)
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def _generate_order_number(self):
        """
        Generate random, unique order number using UUID
        """

        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override original save method to calc the line item
        total and order total
        """

        if not self.order_ref:
            self.order_ref = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return the reference number
        """

        return self.order_ref


class OrderLineItem(models.Model):
    """
    A model for each product when it has been
    ordered
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=False,
        related_name='lineitems'
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False
        )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
        )
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
        )

    def save(self, *args, **kwargs):
        """
        Override original save method to calc line item
        total
        """

        if self.product.sale_price:
            self.lineitem_total = self.product.sale_price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity
        #self.product.stock_quantity = self.product.stock_quantity - self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     """
    #     Override original delete method to re-add
    #     stock quantity to products
    #     """

    #     self.product.stock_quantity = self.product.stock_quantity + self.quantity
    #     print("here")
    #     super().save(*args, **kwargs)

    def __str__(self):
        """
        Return the product name and order ref
        """

        return f'Product "{self.product.name}" on order {self.order.order_ref}'
