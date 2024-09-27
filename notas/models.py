from django.db import models

# Create your models here.
class Nota (models.Model):
    fecha   =   models.DateField()
    usuario =   models.CharField(max_length=15)
    temario =   models.CharField(max_length=15)
    titulo  =   models.CharField(max_length=15)
    apunte  =   models.CharField(max_length=100)

    def __str__(self):
        return str(self.titulo)