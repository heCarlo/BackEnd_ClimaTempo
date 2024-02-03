import uuid
from djongo import models

class ForecastWeatherDataEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    temperature = models.FloatField(max_length=3)
    atmospheric_pressure = models.FloatField(max_length=3)
    moisture = models.FloatField(max_length=3)
    percentage_precipitation = models.FloatField(max_length=3)
    weather_condition = models.CharField(max_length=64)

    class Meta:
        db_table = "forecast_weather_data_entity"

    def __str__(self):
        return (
            f"ForecastWeatherDataEntity [ID: {self.id}, "
            f"Temperature: {self.temperature}, "
            f"Atmospheric Pressure: {self.atmospheric_pressure}, "
            f"Moisture: {self.moisture}, "
            f"Percentage Precipitation: {self.percentage_precipitation}, "
            f"Weather Condition: {self.weather_condition}]"
        )



# template
# como está a previsão (presente passado futuro)
# autenticação
# formulário de cadastro e loguin (CRUD do usuário)

# temperatura
# pressão atmosferica
# humidade
# percentual de preceptação
# condicao climatica

# consultas (passado, futuro, presente) data


# tabela para previsão x tabela historico real
# local de previsão
