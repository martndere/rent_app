from django.urls import path
from . import views

app_name = 'rent'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Home/Dashboard
    path('tenants/', views.tenant_list, name='tenant_list'),
    path('apartments/', views.apartment_list, name='apartment_list'),
    path('payments/', views.payment_list, name='payment_list'),
    path('tenants/<int:tenant_id>/', views.tenant_detail, name='tenant_detail'),
    path('apartments/<int:apartment_id>/', views.apartment_detail, name='apartment_detail'),
    path('payments/<int:payment_id>/', views.payment_detail, name='payment_detail'),
]

