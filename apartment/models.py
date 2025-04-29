from django.db import models

# Create your models here.
class Apartment(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    unit_count = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    owner = models.ForeignKey('landlord.Landlord', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
