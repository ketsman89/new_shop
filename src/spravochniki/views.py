from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from . import models
from . import forms


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
        form = forms.AddCityForm()
        return render(
            request,
            template_name="spravochniki/add-city.html",
        context={"regions": regions, 
                 "greeting": "Add a new city please!", 
                 "form": form})
    else:
        city_form = forms.AddCityForm(request.POST)
        if city_form.is_valid():
            new_city = city_form.save()
        else:
           return render(
                request,
                template_name="spravochniki/add-city.html",
            context={"regions": regions, 
                     "greeting": "Add a new city please!", 
                     "form": form}) 
        print("Is bound?", city_form.is_bound)
        print("Is valid?", city_form.is_valid())
        # new_city = models.City.objects.create(name=city_name, region=region)        
        return HttpResponseRedirect("/added")
    
def update_city(request, pk):
    regions = models.Region.objects.all()    
    if request.method == "GET":
        city = models.City.objects.get(pk=pk)
        return render(
            request,
            template_name="spravochniki/update-city.html",
        context={"object": city, "regions": regions, "greeting": "Edit the city please!"})
    else:
        city_name = request.POST.get("city_name")
        region_id = request.POST.get("region")
        region = models.Region.objects.get(pk=int(region_id))
        print("City", city_name)
        print("Region ID", region_id)
        new_city = models.City.objects.update(name=city_name, region=region)        
        return HttpResponseRedirect("/added")
 
def success_page(request):
     return render(
        request,
        template_name="spravochniki/added-successfully.html",
        context={"message": f"The object was created"})


# Create your views here.
