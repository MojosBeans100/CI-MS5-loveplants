from django.db import models


class Order(models.Model):
    order_ref = models.CharField(max_length=16, null=False, editable=False)
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_num = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address_1 = models.CharField(max_length=80, null=False, blank=False)
    street_address_2 = models.CharField(max_length=80, null=False, blank=True)
    date = models.DateTimeField(auto_now=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False)
    order_total = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False)

