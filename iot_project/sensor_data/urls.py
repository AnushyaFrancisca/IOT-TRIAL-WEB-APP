from django.urls import path
from . import views

urlpatterns = [
    path('api/save_sensor_data/', views.save_sensor_data, name='save_sensor_data'),
    path('api/save_sensor_data/', views.save_sensor_data, name='save_sensor_data'),
    path('chart/', views.sensor_chart, name='sensor_chart'), 
]
