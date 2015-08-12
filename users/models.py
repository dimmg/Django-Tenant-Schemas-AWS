from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    idnp = models.CharField(max_length=13)
    address = models.CharField(max_length=100, blank=True)
    ex_client = models.BooleanField(default=False)
