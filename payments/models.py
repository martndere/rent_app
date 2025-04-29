from django.db import models

# Create your models here.
class Payment(models.Model):
    tenant = models.ForeignKey('tenant.Tenant', on_delete=models.CASCADE)
    bill = models.ForeignKey('bills.Bill', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='pending')  # pending, completed, failed
