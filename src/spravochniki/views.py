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

def add_city(request):
    regions = models.Region.objects.all()    
    if request.method == "GET":
            return render(
            request,
            template_name="spravochniki/add-city.html",
            context={"regions": regions, "greeting": "Add a new city please!"})
    else:
        city_name = request.POST.get("city_name")
        region_id = request.POST.get("region")
        region = models.Region.objects.get(pk=int(region_id))
        print("City", city_name)
        print("Region ID", region_id)
        new_city = models.City.objects.create(name=city_name, region=region)        
        return render(
            request,
            template_name="spravochniki/add-city.html",
            context={"regions": regions, "greeting": f"The city {new_city.name} was created"})
 
def success_page(request):
     return render(
        request,
        template_name="spravochniki/added-successfully.html",
        context={"message": f"The object was created"})


# Create your views here.
