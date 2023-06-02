from typing import Any, Dict, Tuple
from django.db import models
from django import forms

from .choices import condiciones
# informes emitidos
class Libro(models.Model):

    id=models.AutoField(primary_key=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True)
    oficio = models.TextField(verbose_name="Nro. de Oficio", null=True)
    destino = models.CharField(max_length= 100, verbose_name="Oficina de destino", null=True)
    f_emision = models.DateField(null=True, verbose_name="Fecha de emisión")
    f_envio = models.DateField(null=True, verbose_name="Fecha de envío")
    archivo = models.FileField(upload_to='archivos/',verbose_name="Archivo", null=True, blank=True)

    def __str__(self):
        fila = "oficio: " + self.oficio + " - " + "Descripción: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.archivo.storage.delete(self.archivo.name)
        super().delete()

#INFORMES RECIBIDOS
class Libro2(models.Model):

    id=models.AutoField(primary_key=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True)
    oficio = models.TextField(verbose_name="Nro. de Oficio", null=True)
    oficina_emi = models.CharField(max_length= 100, verbose_name="Oficina Emisora", null=True)
    f_recep = models.DateField(null=True, verbose_name="Fecha de recepción")
    archivo = models.FileField(upload_to='archivos/',verbose_name="Archivo", null=True, blank=True)
    marcado = models.BooleanField(default=False, verbose_name="¿Respondido?")

    def __str__(self):
        fila = "Título: " + self.oficio + " - " + "Descripción: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

#SOLICITUDES EMITIDAS
class Libro3(models.Model):

    id=models.AutoField(primary_key=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True)
    oficina_dest = models.CharField(max_length= 100, verbose_name="Oficina Destino", null=True)
    f_emision = models.DateField(null=True, verbose_name="Fecha de emisión")
    archivo = models.FileField(upload_to='archivos/',verbose_name="Archivo", null=True, blank=True)

    def __str__(self):
        fila = "Título: " + self.oficio + " - " + "Descripción: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

#SOLICITUDES RECIBIDAS
class Libro4(models.Model):

    id=models.AutoField(primary_key=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True)
    oficina_emi = models.CharField(max_length= 100, verbose_name="Oficina Emisora", null=True)
    f_recep = models.DateField(null=True, verbose_name="Fecha de recepción")
    archivo = models.FileField(upload_to='archivos/',verbose_name="Archivo", null=True, blank=True)

    def __str__(self):
        fila = "Título: " + self.oficio + " - " + "Descripción: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

#VACACIONES Y COMPENSACIONES
class Libro5(models.Model):

    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True)
    f_recep = models.DateField(null=True, verbose_name="Fecha de recepción")
    archivo = models.FileField(upload_to='archivos/', verbose_name="Archivo", null=True)
    personal = models.ForeignKey('Libro6', null = True, blank = True, on_delete=models.CASCADE )

    def __str__(self):
        fila = "Título: " + str(self.id) + " - " + "Descripción: " + self.descripcion
        return fila


    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

#PERSONAL
class Libro6(models.Model):

    id = models.AutoField(primary_key=True)
    apellido_paterno = models.CharField(null=True, max_length=30, verbose_name="Apellido Paterno")
    apellido_materno = models.CharField(null=True, max_length=30, verbose_name="Apellido Materno")
    nombres = models.CharField(null=True, max_length=50, verbose_name="Nombres")
    condicion = models.CharField(max_length=1, choices=condiciones, default='1')
    dias_rest = models.IntegerField(verbose_name="Vacaciones restantes", null=True, blank = True)

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)

    def __str__(self):
        return self.nombre_completo()
    


