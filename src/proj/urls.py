"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from spravochniki import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spr/', views.home_page),
    path('city/<int:pk>', views.view_city),
    path('city-cbv/<int:pk>', views.CityView.as_view()),
    path('city-delete/<int:pk>', views.delete_city),
    path('city-list-cbv/', views.CityListView.as_view()),
    path('city-delete-cbv/<int:pk>', views.CityDeleteView.as_view()),
    path('city-add/', views.add_city),
    path('city-add-cbv/', views.CityCreateView.as_view()),
    path('added/', views.success_page),
    path('city-update/<int:pk>', views.update_city),
    path('city-update-cbv/<int:pk>', views.CityUpdateView.as_view()),
    path('send-email/', views.send_email),
    path('', views.HomePage.as_view()),

]
