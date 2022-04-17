# 3rd party imports

# Django imports
from django.http import HttpResponse

# Local imports


class StripeWH_Handler:
    """
    Handle Stripe webhooks for order redundancy
    """

    # class of set up method that's called every time an instance
    # of the class is created
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}", status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook event
        """

        return HttpResponse(
            content=f"Webhook received: {event['type']}", status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook event
        """

        return HttpResponse(
            content=f"Webhook received: {event['type']}", status=200)
