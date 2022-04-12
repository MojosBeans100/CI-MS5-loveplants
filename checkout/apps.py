from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'


    # everytime a line item is saved or deleted
    # our custom update total method will be called
    def ready(self):
        import checkout.signals
