from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from . import models
def  home_page(request):
    city_pk = request.GET.get("city")
    print(city_pk)
    cities = models.City.objects.filter(pk=int(city_pk))
    html = "<ul>"
    for city in cities:
        html += f"<li>{city.pk} City {city.name}</li>"
    html += "</ul>"
    return HttpResponse(html)

def view_city(request, pk):
    cities = models.City.objects.filter(pk=int(city_pk))
    html = f"City PK:{city.pk} City name {city.name}"
    return HttpResponse(html)

# Create your views here.
