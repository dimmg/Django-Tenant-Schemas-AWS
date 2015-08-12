from django.db import models


class User(models.Model):
    GENDER = (
        ('-', 'unspecified'),
        ('M', 'male'),
        ('F', 'female')
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    idnp = models.CharField(max_length=13)
    gender = models.CharField(max_length=1, choices=GENDER, default='-') 

