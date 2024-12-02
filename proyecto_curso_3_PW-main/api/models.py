from django.db import models

# Create your models here.
class Campeon(models.Model):
    nombre = models.CharField(max_length=100)
    rasgo_1 = models.CharField(max_length=100)
    rasgo_2 = models.CharField(max_length=100)
    coste = models.IntegerField(None)
    region = models.CharField(max_length=100)