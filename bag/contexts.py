

from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404
from decimal import Decimal
# context processor
# make context dictionary available to all templates across
# application
# 'request' is a built in context processor


def bag_contents(request):
    """
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    standard_delivery = Decimal(str(8.99))

    for item_id, quantity in bag.items():

        product = get_object_or_404(Product, pk=item_id)
        products = Product.objects.all()
        total += quantity * product.price
        product_count += quantity
        product_subtotal = product.price*quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'product_subtotal': product_subtotal,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD and product_count != 0:
        delivery = standard_delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    # look for products around the price of the free delivery delta
    if free_delivery_delta > 0:
        free_delivery_products = products.filter(
                                    price__gte=free_delivery_delta,
                                    stock='in stock').order_by('price')[0:4]

    else:
        free_delivery_products = ""

    # look for products not already in the basket for recommendations
    products_not_in_bag = Product.objects.all()

    for item in bag_items:
        products_not_in_bag.exclude(pk=item['item_id'])

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'standard_delivery': standard_delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'free_delivery_products': free_delivery_products,
        'products_not_in_bag': products_not_in_bag[0:4]
    }

    return context
