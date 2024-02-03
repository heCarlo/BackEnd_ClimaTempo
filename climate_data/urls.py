from django.urls import path, include
from ..climate_data.view import (
    ForecastWeatherDataEntityListView,
    ForecastWeatherDataEntityDetailView,
    create_forecast,
    update_forecast,
    delete_forecast,
)

urlpatterns = [
    path('forecast/', ForecastWeatherDataEntityListView.as_view(), name='forecast-list'),
    path('forecast/<uuid:pk>/', ForecastWeatherDataEntityDetailView.as_view(), name='forecast-detail'),
    path('forecast/create/', create_forecast, name='forecast-create'),
    path('forecast/update/<uuid:pk>/', update_forecast, name='forecast-update'),
    path('forecast/delete/<uuid:pk>/', delete_forecast, name='forecast-delete'),
]
