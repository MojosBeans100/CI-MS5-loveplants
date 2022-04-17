
# 3rd party imports
import stripe

# Django imports
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Local imports
from checkout.webhook_handler import StripeWH_Handler

# Stripe uses webhooks to notify your application when an 
# event happens in your account. Webhooks are particularly
# useful for asynchronous events such as when a customer’s
# bank confirms a payment, a customer disputes a charge, 
# a recurring payment succeeds, or when collecting 
# subscription payments.


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for webhooks from Stripe
    """

    def my_webhook_view(request):

        wh_secret = settings.STRIPE_WH_SECRET
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # get webhook data and verify signature
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                                    payload,
                                    sig_header,
                                    wh_secret
                                    )
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)
        except Exception as e:
            # Other exceptions
            return HttpResponse(content=e, status=400)
        print("Success!")
        return HttpResponse(status=200)
