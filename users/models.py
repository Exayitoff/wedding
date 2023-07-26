from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class User(AbstractUser):
    CHOICES = (
        ('admin', 'Admin'),
        ('owner', 'Owner'),
        ('cutomer', 'Cutomer'),
    )
    
    full_name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(null=True, blank=True)
    is_phone_confirmed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image/', blank=True)
    role = models.CharField(max_length=150, choices=CHOICES, default=True)
    is_active = models.BooleanField(default=True)