from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_individual = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
