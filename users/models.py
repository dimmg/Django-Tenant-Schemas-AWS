from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    idnp = models.CharField(max_length=13)
