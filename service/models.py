from django.db import models
from base.models import BaseModel

from phonenumber_field.modelfields import PhoneNumberField
from base.models import Region, District
from users.models import User

# Create your models here.

class ServiceType(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name}'
    
    
class Service(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone_number = PhoneNumberField(blank=False, null=False)
    additional_phone_number = PhoneNumberField(blank=True, null=True)
    telegram = models.CharField(max_length=250, blank=True, null=True)
    instagram = models.CharField(max_length=250, blank=True, null=True)
    youtube = models.CharField(max_length=250, blank=True, null=True)
    
    def __str__(self):
        return self.title