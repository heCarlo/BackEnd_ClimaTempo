from rest_framework import viewsets
from rest_framework.response import Response
from ..models.forecast_weather_data import ForecastWeatherDataEntity
from ..serializer.forecastWeatherDataSerializer import ForecastWeatherDataEntitySerializer

class ForecastWeatherDataEntityViewSet(viewsets.ModelViewSet):
    queryset = ForecastWeatherDataEntity.objects.all()
    serializer_class = ForecastWeatherDataEntitySerializer

    def list(self, request, *args, **kwargs):
        forecasts = self.queryset
        serializer = self.get_serializer(forecasts, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, *args, **kwargs):
        forecast = self.get_object()
        serializer = self.get_serializer(forecast)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        forecast = self.get_object()
        serializer = self.get_serializer(forecast, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        forecast = self.get_object()
        serializer = self.get_serializer(forecast, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        forecast = self.get_object()
        forecast.delete()
        return Response(status=204)

    # Função personalizada para listar previsões com temperatura acima de 30
    def high_temperature_forecasts(self, request, *args, **kwargs):
        high_temperature_forecasts = self.queryset.filter(temperature__gt=30)
        serializer = self.get_serializer(high_temperature_forecasts, many=True)
        return Response(serializer.data)
