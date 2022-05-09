# 3rd party imports

# Django imports
from django.test import TestCase

# Local imports


class TestViewBag(TestCase):

    def test_render_bag_page(self):
        """
        bag/views.view_bag renders bag.html
        """

        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
