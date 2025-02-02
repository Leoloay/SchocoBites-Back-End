from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name