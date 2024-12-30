from django.shortcuts import render
from .models import Service

def home(request):
    services = Service.objects.all()
    return render(request, 'spa/home.html', {'services': services})
