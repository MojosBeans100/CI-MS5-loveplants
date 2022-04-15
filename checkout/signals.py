
# 3rd party imports

# Django imports
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

# Local imports
from .models import Order, OrderLineItem

# have to update apps.py to let Django know there are new signals

# sender = sender of the signal ie OrderLineItem
# instance = instance of the model that sent it
# created = Boolean send by Django referring to whether 
# this is new instance or one being updated

# we're receiving post save signals from OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on line item update/create
    """

    # ie OrderLineItem.order.update_total()
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on line item delete
    """

    # ie OrderLineItem.order.update_total()
    instance.order_ref.update_total()
