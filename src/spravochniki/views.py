from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from . import models

def  home_page(request):
    cities = models.City.objects.filter(pk__lt=15)
    return render(
        request, 
        template_name="spravochniki/home-page.html", 
        context={'objects': cities })

def view_city(request, pk):
    print(pk)
    city = models.City.objects.get(pk=int(pk))
    return render(
        request, 
        template_name="spravochniki/view-city.html", 
        context={'object': city })

def delete_city(request, pk):
    models.City.objects.get(pk=int(pk)).delete()
    return HttpResponse(f"Object {pk} has been deleted")

# Create your views here.
