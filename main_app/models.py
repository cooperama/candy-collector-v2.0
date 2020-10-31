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
