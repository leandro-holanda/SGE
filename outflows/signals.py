from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from outflows.models import Outflow
from services.notify import Notify


@receiver(post_save, sender=Outflow)
def update_product_quantuty(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()


@receiver(post_save, sender=Outflow)
def send_outflows_event(sender, instance, created, **kwargs):
    notify = Notify()

    try:
        if created:
            data = {
                "event_type": "outflow",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "product": instance.product.title,
                "product_selling_price": float(instance.product.selling_price),
                "product_cost_price": float(instance.product.cost_price),
                "quantity": instance.quantity,
            }
            notify.send_order_event(data)
    except:
        pass
