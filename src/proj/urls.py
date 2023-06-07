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
from django.urls import path, include
from spravochniki import views
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spr/', views.home_page),    
    # path('city-cbv/<int:pk>', views.CityView.as_view(), name="view-city"),    
    # path('city-list-cbv/', views.CityListView.as_view(), name="list-city"),
    # path('city-delete-cbv/<int:pk>', views.CityDeleteView.as_view(), name="delete-city"),    
    # path('city-add-cbv/', views.CityCreateView.as_view(), name="add-city"),
    # path('added/', views.success_page, name="success-page"),    
    # path('city-update-cbv/<int:pk>', views.CityUpdateView.as_view(), name="update-city"),
    # path('send-email/', views.send_email, name="send-email"),
    path('', home_views.HomePage.as_view(), name="home-page"),
    path('spravochniki/', include('spravochniki.urls', namespace='spravochniki'))
    # path('city/<int:pk>', views.view_city),
    # path('city-delete/<int:pk>', views.delete_city),
    # path('city-add/', views.add_city),
    # path('city-update/<int:pk>', views.update_city),

]
