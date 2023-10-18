# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    idcategoria = models.IntegerField(db_column='idCATEGORIA', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Receta(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=150)
    imagen = models.CharField(max_length=100)
    categoria_idcategoria = models.IntegerField(db_column='CATEGORIA_idCATEGORIA')  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'receta'


class Repartidor(models.Model):
    idrepartidor = models.IntegerField(db_column='idREPARTIDOR', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repartidor'
