from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=100)
    car_code = models.CharField(max_length=5)
    car_model = models.CharField(max_length=15)