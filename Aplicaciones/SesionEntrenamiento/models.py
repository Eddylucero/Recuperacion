from django.db import models
from Aplicaciones.PerroDetector.models import PerroDetector
from Aplicaciones.AdiestradorAgricola.models import AdiestradorAgricola

class SesionEntrenamiento(models.Model):
    fecha = models.DateField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    resultado = models.CharField(max_length=255)
    perro = models.ForeignKey(PerroDetector, on_delete=models.CASCADE)  
    adiestrador = models.ForeignKey(AdiestradorAgricola, on_delete=models.CASCADE)  

    def __str__(self):
        return f"Sesión {self.fecha} - {self.perro.nombre} con {self.adiestrador.nombre}"
