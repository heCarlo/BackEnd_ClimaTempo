import uuid
from djongo import models

class RealWeatherDataEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    temperature = models.FloatField(max_length=3)
    atmospheric_pressure = models.FloatField(max_length=3)
    moisture = models.FloatField(max_length=3)
    percentage_precipitation = models.FloatField(max_length=3)
    weather_condition = models.CharField(max_length=64)

    class Meta:
        db_table = "real_weather_data_entity"

    def __str__(self):
        return (
            f"RealWeatherDataEntity [ID: {self.id}, "
            f"Temperature: {self.temperature}, "
            f"Atmospheric Pressure: {self.atmospheric_pressure}, "
            f"Moisture: {self.moisture}, "
            f"Percentage Precipitation: {self.percentage_precipitation}, "
            f"Weather Condition: {self.weather_condition}]"
        )
