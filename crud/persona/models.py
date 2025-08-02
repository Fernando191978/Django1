from django.db import models

class Persona(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    edad = models.IntegerField(verbose_name="Edad")
    email = models.EmailField(verbose_name="Correo Electrónico", max_length=254)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return f"{self.nombre} - {self.email}"
