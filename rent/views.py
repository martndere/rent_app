from django.shortcuts import render
from .models import Tenant, RentPayment, Apartment
from django.utils import timezone

# Dashboard view to display recent tenants, payments, and apartments
def dashboard(request):
    recent_tenants = Tenant.objects.order_by('-move_in_date')[:5]  # Get 5 most recent tenants
    recent_payments = RentPayment.objects.order_by('-date_paid')[:5]  # Corrected model and field
    recent_apartments = Apartment.objects.filter(available=True).order_by('-id')[:5]  # Get 5 most recent available apartments

    context = {
        'recent_tenants': recent_tenants,
        'recent_payments': recent_payments,
        'recent_apartments': recent_apartments
    }

    return render(request, 'rent/home.html', context)

