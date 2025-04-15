from django.db import models
from django.contrib.auth.models import User

# Apartment model
class Apartment(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    water_unit_charge = models.DecimalField(max_digits=6, decimal_places=2)
    electricity_unit_charge = models.DecimalField(max_digits=6, decimal_places=2)
    map_link = models.URLField(blank=True, null=True)
    available = models.BooleanField(default=True)  # Add this field

    def __str__(self):
        return self.name


# Tenant model
class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=20)
    move_in_date = models.DateField()

    def __str__(self):
        return self.user.username

# Rent payment
class RentPayment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)
    paid_for_month = models.DateField()

    def __str__(self):
        return f"{self.tenant.user.username} - {self.paid_for_month.strftime('%B %Y')}"

# Water and electricity usage
class UtilityUsage(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    date_recorded = models.DateField(auto_now_add=True)
    water_units = models.DecimalField(max_digits=6, decimal_places=2)
    electricity_units = models.DecimalField(max_digits=6, decimal_places=2)

    def total_water_cost(self):
        return self.water_units * self.tenant.apartment.water_unit_charge

    def total_electricity_cost(self):
        return self.electricity_units * self.tenant.apartment.electricity_unit_charge

    def __str__(self):
        return f"{self.tenant.user.username} - {self.date_recorded}"

# Security token for tenant access (like a digital gate pass or system key)
class SecurityToken(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tenant.user.username} Token"

