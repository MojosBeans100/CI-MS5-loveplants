
# 3rd party imports

# Django imports
from django.contrib import admin

# Local imports
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Admin model to view all products associated with
    an order
    """

    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin model to view all orders
    """

    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_ref', 'user_profile', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    list_display = ('order_ref', 'date',
                    'full_name', 'order_total',
                    'delivery_cost', 'grand_total',
                    'original_bag', 'stripe_pid')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
