from django.db import models
from django.conf import settings
import os
# Create your models here.
class products(models.Model):
    name = models.CharField(max_length = 500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to = "products/")
    description = models.TextField()
    code = models.CharField(max_length = 100)
    time_placed = models.TimeField(auto_now_add=True)
    available_quantity = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} -- {self.price}"
