from django.db import models


class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    facultad = models.CharField(max_length=100)
    duracion_anios = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100) 
    codigo = models.CharField(max_length=20, unique=True)
    semestre = models.PositiveIntegerField()
    programa = models.ForeignKey(
        Programa, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
        

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    codigo_estudiante = models.CharField(max_length=20, unique=True)
    fecha_ingreso = models.DateField()
    programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
    cursos = models.ManyToManyField(Curso, related_name='estudiantes', blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo_estudiante})"


# Create your models here.
