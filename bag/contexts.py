

from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404
from decimal import Decimal
# context processor
# make context dictionary available to all templates across
# application
# 'request' is a built in context processor


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():

        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD and product_count != 0:
        delivery = Decimal(str(8.99))
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    # look for products around the price of the free delivery delta
    if free_delivery_delta > 0:
        free_delivery_delta_20 = free_delivery_delta*Decimal(str(1.2))
        free_delivery_products = Product.objects.filter(price__gte=free_delivery_delta,
                                    price__lte=free_delivery_delta_20)
    else:
        free_delivery_products = ""

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'free_delivery_products': free_delivery_products,
    }

    return context
