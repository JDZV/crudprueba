# Importa el módulo de modelos de Django
from django.db import models

# Define el modelo 'Sensores' que contendrá datos relacionados con sensores
class Sensores(models.Model):
    acc = models.IntegerField()  # Campo para la aceleración
    di1 = models.IntegerField()  # Campo para la entrada digital 1
    towing = models.IntegerField()  # Campo para indicar si está remolcando algo

# Define el modelo 'Position' que contendrá datos de ubicación (latitud y longitud)
class Position(models.Model):
    lat = models.FloatField()  # Campo para la latitud
    lon = models.FloatField()  # Campo para la longitud

# Define el modelo 'GPS' que contendrá datos generales y referencias a 'Sensores' y 'Position'
class GPS(models.Model):
    imei = models.CharField(max_length=20)  # Campo para el IMEI del dispositivo GPS
    position = models.OneToOneField(Position, on_delete=models.CASCADE, null=True)  # Relación uno a uno con 'Position'
    alt = models.FloatField()  # Campo para la altitud
    speed = models.FloatField()  # Campo para la velocidad
    orientation = models.FloatField()  # Campo para la orientación
    sensores = models.OneToOneField(Sensores, on_delete=models.CASCADE, null=True)  # Relación uno a uno con 'Sensores'
    fecha_hora = models.DateTimeField(auto_now_add=True)  # Campo para la fecha y hora, se establece automáticamente al crear el objeto


