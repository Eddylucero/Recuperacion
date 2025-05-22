from django.db import models

class AdiestradorAgricola(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=100)
    experiencia = models.IntegerField(help_text="Años de experiencia")

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"
