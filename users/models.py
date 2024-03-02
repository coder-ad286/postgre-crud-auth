from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    last_login = None
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]

