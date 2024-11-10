from django.db import models

class Encuesta(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    comuna = models.CharField(max_length=100)
    correo = models.EmailField()
    pregunta1 = models.BooleanField()
    pregunta2 = models.BooleanField()
    pregunta3 = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} - {self.comuna}'
