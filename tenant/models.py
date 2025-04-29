from django.db import models
from django.conf import settings

# Create your models here.
class Tenant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    apartment = models.ForeignKey('apartment.Apartment', on_delete=models.SET_NULL, null=True)
    move_in_date = models.DateField()
    is_active = models.BooleanField(default=True)
