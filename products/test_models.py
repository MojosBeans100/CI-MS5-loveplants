# 3rd party imports

# Django imports
from django.test import TestCase
from django.contrib.auth.models import User

# Local imports
from .models import Product


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
            plant_category='Potted',
            latin_name='latin name',
            description='this is the description',
            description_source='text',
            description_url='url.com',
            image1_source='text',
            image1_source_url='url.com',
            image2_source='text',
            image2_source_url='url.com',
            image3_source='text',
            image3_source_url='url.com',
            pot_size=10,
            height=10,
            price=10,
            stock_quantity=10,
            maturity_num=10,
            maturity_time='months',
            sunlight='low',
            watering='low',
            care_required='can stand a little neglect',
            care_instructions='text',
            care_instructions_source='text',
            care_instructions_url='url.com',
            rare=True,
            popular=True,
            live_on_site=True,
            average_rating=0,
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
