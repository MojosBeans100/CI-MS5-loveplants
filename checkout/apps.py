# 3rd party imports

# Django imports
from django.apps import AppConfig

# Local imports


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
