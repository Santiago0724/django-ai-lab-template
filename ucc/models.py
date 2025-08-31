from django.db import models

class Programa(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='cursos')
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=120)
    creditos = models.PositiveSmallIntegerField(default=3)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Estudiante(models.Model):
    codigo = models.CharField(max_length=12, unique=True, default="0000") 
    nombre = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    # Relación muchos a muchos vía tabla intermedia Inscripcion
    cursos = models.ManyToManyField('Curso', through='Inscripcion', related_name='estudiantes')

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['estudiante', 'curso'], name='unique_inscripcion')
        ]

    def __str__(self):
        return f"{self.estudiante} → {self.curso}"
