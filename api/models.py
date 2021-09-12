from django.db import models

# Create your models here.

class Product(models.Model):
    customer_name = models.TextField(max_length=200, null=True, blank=True)
    product_name = models.TextField(max_length=500, null=True, blank=True)
    customer_phone = models.IntegerField(null=True, blank=True, default=91)
    customer_address = models.TextField(max_length=500, null=True, blank=True)
    OrderAt = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')


    def __str__(self):
        return str(self.id)
