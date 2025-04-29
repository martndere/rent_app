from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from .models import Apartment
from django.urls import reverse_lazy

class ApartmentListView(ListView):
    model = Apartment
    template_name = 'apartment/apartment_list.html'

class ApartmentDetailView(DetailView):
    model = Apartment
    template_name = 'apartment/apartment_detail.html'

class ApartmentCreateView(CreateView):
    model = Apartment
    fields = ['name', 'location', 'unit_count', 'description', 'owner']
    template_name = 'apartment/apartment_form.html'
    success_url = reverse_lazy('apartment_list')
