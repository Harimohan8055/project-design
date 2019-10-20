from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_individual = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    is_confirm = models.BooleanField(default=False)


class IndividualProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    location = models.CharField(max_length=15)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


class InstitutionProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institutionname = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    location = models.CharField(max_length=15)
    regno = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
