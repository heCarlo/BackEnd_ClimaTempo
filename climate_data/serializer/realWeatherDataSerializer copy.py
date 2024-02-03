from rest_framework import serializers
from ..models.real_weather_data import RealWeatherDataEntity

class RealWeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealWeatherDataEntity
        fields = '__all__'
