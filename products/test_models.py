# 3rd party imports
import datetime

# Django imports
from django.test import TestCase
from django.contrib.auth.models import User

# Local imports
from .models import Product, ProductReview


class TestProductModel(TestCase):
    """
    test the product model returns auto calculated
    values
    """

    def setUp(self):

        user = User.objects.create(
            username='Lucy',
            password='Mojo',
        )

        product = Product.objects.create(
            friendly_name='A New Product',
            price=50.00,
        )

        product_review1 = ProductReview(
            product=product,
            rating=5,
            user=user,  
        )

        product_review2 = ProductReview(
            product=product,
            rating=5,
            user=user,  
        )

    def test_product_str_method(self):
        """
        test the model string method
        """

        product = Product.objects.get()
        self.assertEqual(product.__str__(), 'A New Product')

    def test_product_name_method(self):
        """
        test that the product name is the slug
        of the friendly name
        """

        product = Product.objects.get()
        self.assertEqual(product.name, 'a_new_product')
