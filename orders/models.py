from django.db import models 
from django.contrib.auth.models import User


class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nam} (${self.price})




class Order(models.Model):

    ORDER_STATUS_CHOICES=[
        ('PENDING','Pending'),
        ('PROCESSING','Processing'),
        ('SHIPPED','Shipped'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled'),

    ]

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        help_text="Teh customer who placed the order."
    )
    order_items = models.ManyToManyField(
        Menu,
        related_name='orders',
        help_text="The menu items included in this order."
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="The total amount of the order."
    )
    order_status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default='PENDING',
        help_text="The current status of the order."
    )

    def __str__(self):

        return f"Order #{self.id} by {self.customer.get_full_name() or self.customer.username}"