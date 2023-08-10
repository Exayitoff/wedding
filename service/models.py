from django.db import models
from base.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField
from base.models import Region, District
from users.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class ServiceType(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name}'
    
class Service(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    people_count = models.PositiveIntegerField(validators=[MinValueValidator(0)], blank=True, null=True) 
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='regions', blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='districts', blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone_number = PhoneNumberField(unique=True)
    additional_phone_number = PhoneNumberField(blank=True, null=True)
    telegram = models.URLField(max_length=250, blank=True, null=True)
    instagram = models.URLField(max_length=250, blank=True, null=True)
    youtube = models.URLField(max_length=250, blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)    
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    def str(self):
        return self.title