from django.db import models

class PerroDetector(models.Model):
    nombre = models.CharField(max_length=255)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    estado = models.CharField(max_length=50, choices=[("En progreso", "En progreso"), ("Certificado", "Certificado")])

    def __str__(self):
        return f"{self.nombre} ({self.raza})"
