from django.contrib import admin
from django.urls import include, path
from ..climate_data.urls import urlpatterns

urlpatterns = [
    path('forestWeatherData/', include('climate_data.urls')),
    ]
