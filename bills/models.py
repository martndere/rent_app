from django.db import models

# Create your models here.
class Bill(models.Model):
    apartment = models.ForeignKey('apartment.Apartment', on_delete=models.CASCADE)
    bill_type = models.CharField(max_length=50)  # e.g., water, electricity
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
