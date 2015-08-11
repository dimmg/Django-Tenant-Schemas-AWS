from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    idnp = models.CharField(max_length=13)
    ex_client = models.BooleanField(default=False)

