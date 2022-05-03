# 3rd party imports
import datetime

# Django imports
from django.test import TestCase
from django.contrib.auth.models import User

# Local imports
from products.models import Product, ProductReview
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile


class TestProfileView(TestCase):
    """
    test the profile view page
    """

    def setUp(self):

        user = User.objects.create(
            username='Mojo',
            password='ilovetennisballs',
            is_superuser=False
        )

        user2 = User.objects.create(
            username='not_user',
            password='12345',
            is_superuser=False
        )

    def test_return_profile_page(self):
        """
        test profiles/profile.html returns correct
        user profile
        """

        user = User.objects.get(id=1)
        self.client.force_login(User.objects.get(id=1))
        response = self.client.get(
            '/profiles/profile.html'
            )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('/profiles/profile.html')
        self.assertEqual(
            response.context['user_profile'].username,
            user.username
            )

    def test_return_correct_orders(self):
        """
        test that only user's orders are returned
        """

        user_profile = UserProfile.objects.get(id=1)
        user_profile2 = UserProfile.objects.get(id=2)

        order = Order.objects.create(
            order_ref="MyOrder999",
            user_profile=user_profile,
            full_name='Mojo',
            email='mojo@pawprints.com',
            phone_num='04365465',
            street_address_1='The Orchard',
            street_address_2='The Garden',
            town_or_city='Paradise',
            county='Paradise',
            postcode='546hfghf',
            date=datetime.datetime.now(),
            delivery_cost=1.00,
            order_total=30.00,
            grand_total=31.00,
            original_bag='two tennis balls',
            stripe_pid='rtyr74645'
        )

        order2 = Order.objects.create(
            order_ref="MyOrder999",
            user_profile=user_profile2,
            full_name='Mojo',
            email='mojo@pawprints.com',
            phone_num='04365465',
            street_address_1='The Orchard',
            street_address_2='The Garden',
            town_or_city='Paradise',
            county='Paradise',
            postcode='546hfghf',
            date=datetime.datetime.now(),
            delivery_cost=1.00,
            order_total=30.00,
            grand_total=31.00,
            original_bag='two tennis balls',
            stripe_pid='rtyr74645'
        )

        orders = Order.objects.all()

        self.client.force_login(User.objects.get(id=1))
        response = self.client.get(
            '/profiles/profile.html'
            )

        self.assertEqual(len(orders), 2)
        self.assertEqual(len(response.context['orders']), 1)
        self.assertEqual(
            (response.context['orders'][0].order_ref),
            order.order_ref
            )