from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True)
    birth = models.DateField()
    gender = models.CharField(max_length=10, null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    