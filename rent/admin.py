from django.contrib import admin
from .models import Apartment, Tenant, RentPayment, UtilityUsage, SecurityToken

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price_per_month', 'available')
    search_fields = ('name', 'location')
    list_filter = ('available',)

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('user', 'apartment', 'phone', 'move_in_date')
    search_fields = ('user__username', 'apartment__name')

@admin.register(RentPayment)
class RentPaymentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'amount', 'date_paid', 'paid_for_month')
    list_filter = ('date_paid',)

@admin.register(UtilityUsage)
class UtilityUsageAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'date_recorded', 'water_units', 'electricity_units')

@admin.register(SecurityToken)
class SecurityTokenAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'token', 'created_at', 'is_active')
    list_filter = ('is_active',)

