from django.db import models

# Create your models here.


class Propietario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)
    cedula = models.CharField(max_length=10)
    estado = models.BooleanField

    def __str__(self):
        return self.nombre


class Inmueble(models.Model):
    torre = models.CharField(max_length=10)
    piso = models.CharField(max_length=10)
    apartamento = models.CharField(max_length=5)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.apartamento


class Vehiculo(models.Model):
    placa = models.CharField(max_length=6)
    modelo = models.CharField(max_length=15)
    color = models.CharField(max_length=10)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa


class Puesto(models.Model):
    numero = models.CharField(max_length=5)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.numero