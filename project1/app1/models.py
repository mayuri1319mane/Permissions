from django.db import models

# Create your models here.
class Mobile(models.Model):
    mname=models.CharField(max_length=30)
    mclr = models.CharField(max_length=20)
    mfeatures = models.CharField(max_length=40)
    ram = models.CharField(max_length=20)
    rom = models.CharField(max_length=20)
    version = models.CharField(max_length=30)
    price = models.FloatField()
    date = models.DateField()
    owner = models.CharField(max_length=30)
