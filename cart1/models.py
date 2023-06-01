from django.db import models
from django.contrib.auth.models import User
from myapp.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        order_items = self.order_items.all()
        self.total_price = sum(item.total_product_price for item in order_items)
        super().save(update_fields=['total_price'])
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total_product_price = self.price * self.quantity
        super().save(*args, **kwargs)
        order_items = self.order.order_items.all()
        self.order.total_price = sum([item.total_product_price for item in order_items])
        self.order.save()

