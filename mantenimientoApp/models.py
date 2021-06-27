from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid

# Create your models here.


class estado(models.Model):
    estado=models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.estado

class color(models.Model):
    nombre_color=models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.nombre_color

class medio_contacto(models.Model):
    descripcion=models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.descripcion

class distrito(models.Model):
    cod_postal=models.CharField(max_length=30, blank=True, null=True)
    nombre_distrito=models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.nombre_distrito


class tipo_mascota(models.Model):
    tipo=models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.tipo



class albergues(models.Model):
    nombre_albergue=models.CharField(max_length=50, blank=True, null=True)
    ciudad=models.CharField(max_length=30, blank=True, null=True)
    direccion=models.CharField(max_length=1000, blank=True, null=True)
    id_distrito=models.ForeignKey(
        distrito, on_delete=models.CASCADE, blank=True, null=True)
    referencia=models.CharField(max_length=11000, blank=True, null=True)
    duena=models.CharField(max_length=100, blank=True, null=True)
    responsable=models.CharField(max_length=100, blank=True, null=True)
    cuidador=models.CharField(max_length=100, blank=True, null=True)
    dias_atencion=models.CharField(max_length=100, blank=True, null=True)
    horario_atencion=models.CharField(max_length=100, blank=True, null=True)
    fecha_ingreso_matchcota=models.DateField(blank=True, null=True)
    vigente=models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.nombre_albergue


class detalle_puesto(models.Model):
    puesto=models.CharField(max_length = 254,blank=True, null=True, verbose_name='Puesto')

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
    #   """
        return self.puesto