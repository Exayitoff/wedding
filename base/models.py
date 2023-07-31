from django.db import models
from django.conf import settings



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='%. (class)s_created_by', null=True, blank=True)
    # updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_updated_by', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        abstract=True
