# 3rd party imports

# Django imports
from django.test import TestCase

# Local imports


class TestHomeViews(TestCase):
    """
    Test views in the home app
    """

    def test_render_homepage(self):
        """
        home/views.index renders index.html
        """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
