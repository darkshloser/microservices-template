from django.db import models
import uuid


class Order(models.Model):
    OPEN = 'open'
    CLOSE = 'close'

    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (CLOSE, 'Close'),
    ]

    title = models.CharField(max_length=200)
    table = models.CharField(max_length=200)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default=OPEN)

    class Meta:
        db_table = 'api_order'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product_id = models.UUIDField(default=uuid.uuid4, editable=False)
    product_title = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product_title} in order {self.order.title}"

    class Meta:
        db_table = 'api_orderitem'

