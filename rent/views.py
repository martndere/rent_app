from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Apartment, Tenant, RentPayment, UtilityUsage, SecurityToken

@login_required
def dashboard(request):
    # Get counts for dashboard cards
    apartment_count = Apartment.objects.count()
    tenant_count = Tenant.objects.count()
    available_apartments = Apartment.objects.filter(available=True).count()
    
    # Get recent activities
    recent_payments = RentPayment.objects.order_by('-date_paid')[:5]
    recent_utility_usage = UtilityUsage.objects.order_by('-date_recorded')[:5]
    
    context = {
        'apartment_count': apartment_count,
        'tenant_count': tenant_count,
        'available_apartments': available_apartments,
        'recent_payments': recent_payments,
        'recent_utility_usage': recent_utility_usage,
    }
    return render(request, 'rent/home.html', context)

@login_required
def tenant_list(request):
    tenants = Tenant.objects.select_related('user', 'apartment').all()
    context = {'tenants': tenants}
    return render(request, 'rent/tenant_list.html', context)

@login_required
def tenant_detail(request, tenant_id):
    tenant = get_object_or_404(Tenant.objects.select_related('user', 'apartment'), pk=tenant_id)
    payments = RentPayment.objects.filter(tenant=tenant).order_by('-paid_for_month')
    utility_usages = UtilityUsage.objects.filter(tenant=tenant).order_by('-date_recorded')
    tokens = SecurityToken.objects.filter(tenant=tenant, is_active=True)
    
    context = {
        'tenant': tenant,
        'payments': payments,
        'utility_usages': utility_usages,
        'tokens': tokens,
    }
    return render(request, 'rent/tenant_detail.html', context)

@login_required
def apartment_list(request):
    apartments = Apartment.objects.all()
    context = {'apartments': apartments}
    return render(request, 'rent/apartment_list.html', context)

@login_required
def apartment_detail(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    tenants = Tenant.objects.filter(apartment=apartment).select_related('user')
    
    context = {
        'apartment': apartment,
        'tenants': tenants,
    }
    return render(request, 'rent/apartment_detail.html', context)

@login_required
def payment_list(request):
    payments = RentPayment.objects.select_related('tenant__user', 'tenant__apartment').order_by('-date_paid')
    context = {'payments': payments}
    return render(request, 'rent/payment_list.html', context)

@login_required
def payment_detail(request, payment_id):
    payment = get_object_or_404(
        RentPayment.objects.select_related('tenant__user', 'tenant__apartment'), 
        pk=payment_id
    )
    context = {'payment': payment}
    return render(request, 'rent/payment_detail.html', context)

