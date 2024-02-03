from rest_framework import serializers
from ..models.forecast_weather_data import ForecastWeatherDataEntity

class ForecastWeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastWeatherDataEntity
        fields = '__all__'
