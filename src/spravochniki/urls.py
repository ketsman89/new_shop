from django.urls import path
from . import views

app_name = "spravochniki"
urlpatterns = [    
    path('city-cbv/<int:pk>', views.CityView.as_view(), name="view-city"),    
    path('city-list-cbv/', views.CityListView.as_view(), name="list-city"),
    path('city-delete-cbv/<int:pk>', views.CityDeleteView.as_view(), name="delete-city"),    
    path('city-add-cbv/', views.CityCreateView.as_view(), name="add-city"),
    path('added/', views.success_page, name="success-page"),    
    path('city-update-cbv/<int:pk>', views.CityUpdateView.as_view(), name="update-city"),
    path('send-email/', views.send_email, name="send-email"),
    # path('city/<int:pk>', views.view_city),
    # path('city-delete/<int:pk>', views.delete_city),
    # path('city-add/', views.add_city),
    # path('city-update/<int:pk>', views.update_city),

]
