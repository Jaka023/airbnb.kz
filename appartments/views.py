from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Appartments


class AppartmentsList(ListView):
    model = Appartments
    template_name = 'appartments/appartments_list.html'
    paginate_by = 10
    queryset = Appartments.objects.all()


class AppartmentDetail(DetailView):
    model = Appartments
    template_name = 'appartments/appartments_detail.html'