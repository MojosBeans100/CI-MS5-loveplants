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

    def test_return_profile_page(self):
        """
        test profiles/profile.html returns correct
        user profile
        """

        user = User.objects.get()
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