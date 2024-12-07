from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userName = models.CharField(max_length=150, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(default=0)  # Set default value for age
    phone = models.CharField(max_length=20, default='')  # Default empty string for phone
    dateOfBirth = models.DateTimeField(default=timezone.now, null=True)  # Default None for dateOfBirth
    nationalityCountry = models.CharField(max_length=100, default='')  # Default empty string
    nationalityCity = models.CharField(max_length=100, default='')  # Default empty string
    residenceCountry = models.CharField(max_length=100, default='')  # Default empty string
    residenceCity = models.CharField(max_length=100, default='')  # Default empty string
    profilePicture = models.URLField(default='')  # Default empty string for URL
    latitude = models.FloatField(default=0.0)  # Default 0.0 for latitude
    longitude = models.FloatField(default=0.0)  # Default 0.0 for longitude

    objects = models.Manager()

    def __str__(self):
        return f'{self.firstName} {self.lastName} ({self.userName})'