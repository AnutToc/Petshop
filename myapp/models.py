from django.db import models
from django.urls import reverse

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=128, default='default_password')

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})
    
