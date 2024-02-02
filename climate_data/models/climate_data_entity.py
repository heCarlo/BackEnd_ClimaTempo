from django.db import models


class ClimateDataEntity(models.model):
    temperature = models.FloatField()
    atmospheric_pressure = models.FloatField()
    moisture = models.FloatField()
    percentage_precipitation = models.FloatField()
    weather_condition = models.FloatField()

    def __str__(self):
        return "temperature"


#template
#como está a previsão (presente passado futuro)
#autenticação
#formulário de cadastro e loguin (CRUD do usuário)
    
    #temperatura
    #pressão atmosferica
    #humidade
    #percentual de preceptação
    #condicao climatica

    #consultas (passado, futuro, presente)


    #tabela para previsão x tabela historico real
    #local de previsão