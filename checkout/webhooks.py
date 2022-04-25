
# 3rd party imports
import stripe

# Django imports
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Local imports
from checkout.webhook_handler import StripeWH_Handler
import os


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for webhooks from Stripe
    """

    wh_secret = os.environ.get('STRIPE_WH_SECRET')
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
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
        return HttpResponse(status=400, content=e)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400, content=e)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    handler = StripeWH_Handler(request)
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_intent_payment_failed,
    }

    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)
    response = event_handler(event)
    return response
