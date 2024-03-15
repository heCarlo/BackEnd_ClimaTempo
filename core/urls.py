from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('forestWeatherData/', include('climate_data.urls')),
    ]
