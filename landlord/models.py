from django.db import models
from django.conf import settings

# Create your models here.
class Landlord(models.Model):
    uuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=20)
