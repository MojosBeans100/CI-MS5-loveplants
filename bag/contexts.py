# 3rd party imports
from decimal import Decimal

# Django imports
from django.conf import settings
from django.shortcuts import get_object_or_404

# Local imports
from products.models import Product


def bag_contents(request):
    """
    Create session of bag contents
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    standard_delivery = Decimal(str(8.99))

    for item_id, quantity in bag.items():

        product = get_object_or_404(Product, pk=item_id)
        products = Product.objects.all()
        if product.sale_price:
            total += quantity * product.sale_price
            product_count += quantity
            product_subtotal = product.sale_price*quantity
        else:
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

    if free_delivery_delta > 0:
        free_delivery_products = products.filter(
                                    price__gte=free_delivery_delta,
                                    live_on_site=True).order_by('price')[0:4]

    else:
        free_delivery_products = None

    excludes = []
    for item in bag_items:
        excludes.append(int(item['item_id']))

    products_not_in_bag = Product.objects.exclude(pk__in=excludes)

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
        'products_not_in_bag': products_not_in_bag[0:4],
        'all_products': Product.objects.all(),
    }

    return context
