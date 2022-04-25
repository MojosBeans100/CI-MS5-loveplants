
# 3rd party imports

# Django imports
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

# Local imports
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on line item update/create
    """

    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on line item delete
    """

    instance.order.update_total()
