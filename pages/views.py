from django.shortcuts import render
from .models import Slider
from appartments.models import Appartments

def index(request):
    slides = Slider.objects.all()
    apt = Appartments.objects.all()
    return render(request, 'home.html', {'slides': slides, 'apt' : apt})

def about(request):
    return render(request, 'pages/about.html')

def contacts(request):
    return render(request, 'pages/contacts.html')