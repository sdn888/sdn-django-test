from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=30)
    address = models.TextField(max_length=30)