# 3rd party imports
import datetime

# Django imports
from django.test import TestCase
from django.contrib.auth.models import User

# Local imports
from .models import Product, ProductReview
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from .forms import ProductForm, ProductReviewForm


class TestProductViews(TestCase):
    """
    Test views in the products app
    """

    def setUp(self):

        test_user = User.objects.create(
            username='Hello',
            password='12345',
        )

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
            care_required='high',
            care_instructions='care instruct',
            care_instructions_source='care source',
            care_instructions_url='care.com',
            rare=False,
            popular=False,
            live_on_site=False,
            average_rating=0
        )

        product3 = Product.objects.create(
            name='test2_product',
            friendly_name='Test3 product',
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
            care_required='high',
            care_instructions='care instruct',
            care_instructions_source='care source',
            care_instructions_url='care.com',
            rare=False,
            popular=False,
            live_on_site=False,
            average_rating=0
        )

        order = Order.objects.create(
            order_ref='12345',
            user_profile=UserProfile.objects.get(id=1),
            full_name='Lucy',
            email='lucybabucy.com',
            street_address_1='1',
            street_address_2='2',
            phone_num='06949',
            town_or_city='3',
            county='4',
            postcode='5',
            date=datetime.date.today(),
            delivery_cost=0,
            order_total=0,
            grand_total=0,
            original_bag='bag',
            stripe_pid='6745645'
        )

        orderlineitem = OrderLineItem.objects.create(
            order=order,
            product=product1,
            quantity=5,
            lineitem_total=50,
        )

        order3 = Order.objects.create(
            order_ref='43545',
            user_profile=UserProfile.objects.get(id=1),
            full_name='Lucy',
            email='lucybabucy.com',
            street_address_1='1',
            street_address_2='2',
            phone_num='06949',
            town_or_city='3',
            county='4',
            postcode='5',
            date=datetime.date.today(),
            delivery_cost=0,
            order_total=0,
            grand_total=0,
            original_bag='bag',
            stripe_pid='6745645'
        )

        orderlineitem3 = OrderLineItem.objects.create(
            order=order,
            product=product3,
            quantity=5,
            lineitem_total=50,
        )

        productreview = ProductReview.objects.create(
            rating=5,
            product=product1,
            user=test_user,
            review='I love this product',
            review_time=datetime.date.today(),
            review_time_ago='5',
            liked=True
        )

        productreview2 = ProductReview.objects.create(
            rating=3,
            product=product2,
            user=test_user,
            review='I love this product yay',
            review_time=datetime.date.today(),
            review_time_ago='0',
            liked=False
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

    def test_product_detail_returns_correct_product(self):
        """
        views.product_detail renders product_detail/id
        """
        product = Product.objects.get(id=1)
        response = self.client.get(f'/products/product_detail/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['product'], Product)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_detail_returns_correct_product_reviews(self):
        """
        views.product_detail returns only related product reviews
        """

        product = Product.objects.get(id=1)
        response = self.client.get(f'/products/product_detail/{product.id}')
        self.assertEquals(
            response.context['reviews'][0].product, response.context['product']
            )

    def test_if_critera_render_criteria_products(self):
        """
        views.product_detail returns other rare, popular or easy
        care products if product is rare
        """

        # product is rare, popular, easy care
        product1 = Product.objects.get(id=1)
        response1 = self.client.get(f'/products/product_detail/{product1.id}')
        self.assertIsNotNone(response1.context['rare_products'])
        self.assertIsNotNone(response1.context['popular_products'])
        self.assertIsNotNone(response1.context['easy_care'])

        # product is NOT rare, popular, or easy care
        product2 = Product.objects.get(id=2)
        response2 = self.client.get(f'/products/product_detail/{product2.id}')
        self.assertIsNone(response2.context['rare_products'])
        self.assertIsNone(response2.context['popular_products'])
        self.assertIsNone(response2.context['easy_care'])

    def test_product_liked(self):
        """
        views.product_detail returns liked = true
        if user has liked or not liked product
        """

        self.client.force_login(User.objects.get(id=1))
        product1 = Product.objects.get(id=1)
        response1 = self.client.get(f'/products/product_detail/{product1.id}')
        self.assertEqual(response1.context['reviews'][0].liked, True)
        self.assertEqual(True, response1.context['liked'])
        self.assertEqual(
            response1.context['reviews'][0].liked,
            response1.context['liked']
            )

        product2 = Product.objects.get(id=2)
        response2 = self.client.get(f'/products/product_detail/{product2.id}')
        self.assertEqual(response2.context['reviews'][0].liked, False)
        self.assertEqual(False, response2.context['liked'])
        self.assertEqual(
            response2.context['reviews'][0].liked,
            response2.context['liked']
            )

    def test_view_renders_form(self):
        """
        view.product_detail renders form if the user
        has purchased the product, form is None if user
        has already reviewed or has not purchased
        """

        self.client.force_login(User.objects.get(id=1))
        product1 = Product.objects.get(id=1)
        product2 = Product.objects.get(id=2)
        product3 = Product.objects.get(id=3)

        # has purchased, has reviewed ie don't display form
        response1 = self.client.get(f'/products/product_detail/{product1.id}')
        self.assertIsNone(response1.context['form'])
        self.assertEqual(response1.context['has_purchased'], True)
        self.assertEqual(response1.context['already_reviewed'], True)

        # has NOT purchased, do not display form
        response2 = self.client.get(f'/products/product_detail/{product2.id}')
        self.assertIsNone(response2.context['form'])
        self.assertEqual(response2.context['has_purchased'], False)

        # has purchased, has NOT reviewed ie display form
        response3 = self.client.get(f'/products/product_detail/{product3.id}')
        self.assertIsNotNone(response3.context['form'])
        self.assertEqual(response3.context['has_purchased'], True)
        self.assertEqual(response3.context['already_reviewed'], False)