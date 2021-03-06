from django.db import models
from django.urls import reverse #
from django.contrib.auth.models import User



class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.store_name



class Candy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=50)

    seller = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def in_stock(self):
        if self.stock <= 0:
            return "Out of Stock"
        elif self.stock <= 10:
            return "Limited Quantity!"

