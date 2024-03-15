from django.urls import path, include
from .view.ForecastWeatherDataView import ForecastWeatherDataEntityViewSet

urlpatterns = [
    path('forecast/', ForecastWeatherDataEntityViewSet.as_view({'get': 'list', 'post': 'create'}), name='forecast-list'),
]
