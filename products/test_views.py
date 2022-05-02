# 3rd party imports

# Django imports
from django.test import TestCase
from django.contrib.auth.models import User

# Local imports
from .models import Product, ProductReview
from .forms import ProductForm, ProductReviewForm

class TestProductViews(TestCase):
    """
    Test views in the products app
    """

    def setUp(self):
        product1 = Product.objects.create(
            name='test_product',
            friendly_name='Test product',
            latin_name='test_latin_name',
            description='description',
            description_source='description source',
            description_url='description.com',
            image1_source='image1_source',
            image1_source_url='image1.com',
            image2_source='image2_source',
            image2_source_url='image2.com',
            image3_source='image3_source',
            image3_source_url='image3.com',
            price=20.00,
            sale_price=0,
            stock_quantity=5,
            pot_size=10,
            height=10,
            length=10,
            maturity_num=2,
            maturity_time='months',
            sunlight='med',
            watering='med',
            care_required='low',
            care_instructions='care instruct',
            care_instructions_source='care source',
            care_instructions_url='care.com',
            rare=True,
            popular=True,
            live_on_site=True,
            average_rating=0
        )

        product2 = Product.objects.create(
            name='test2_product',
            friendly_name='Test2 product',
            latin_name='test_latin_name',
            description='description',
            description_source='description source',
            description_url='description.com',
            image1_source='image1_source',
            image1_source_url='image1.com',
            image2_source='image2_source',
            image2_source_url='image2.com',
            image3_source='image3_source',
            image3_source_url='image3.com',
            price=20.00,
            sale_price=0,
            stock_quantity=5,
            pot_size=10,
            height=10,
            length=10,
            maturity_num=2,
            maturity_time='months',
            sunlight='med',
            watering='med',
            care_required='low',
            care_instructions='care instruct',
            care_instructions_source='care source',
            care_instructions_url='care.com',
            rare=True,
            popular=True,
            live_on_site=False,
            average_rating=0
        )

        superuser = User.objects.create(
            is_superuser=True,
            username='Superuser',
            password='54321',
        )

    def test_get_products_page(self):
        """
        product/views.all_products renders products.html
        """
        response = self.client.get('/products/products.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_products_renders_live_products(self):
        """
        product/views.all_products only displays live products
        to non superuser
        """

        self.user = User.objects.create(
            is_superuser=False,
            username='Non super',
            password='12345',
        )
        self.client.login(username='Non super', password='12345')
        response = self.client.get('/products/products.html')
        self.assertEqual(len(response.context['all_products']), 1)
        self.assertEqual(
            response.context['all_products'][0].friendly_name, 'Test product'
            )
        self.assertEqual(
            len(response.context['all_products'].filter(
                friendly_name='Test2 product')), 0)

    def test_products_renders_all_products(self):
         """
        product/views.all_products only displays live products
        to non superuser
        """

        self.user = User.objects.create(
            is_superuser=False,
            username='Non super',
            password='12345',
        )
        self.client.login(username='Non super', password='12345')
        response = self.client.get('/products/products.html')
        self.assertEqual(len(response.context['all_products']), 1)
        self.assertEqual(
            response.context['all_products'][0].friendly_name, 'Test product'
            )
        self.assertEqual(
            len(response.context['all_products'].filter(
                friendly_name='Test2 product')), 0)