from django.contrib import admin
from .models import Programa, Curso, Estudiante


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "facultad", "duracion_anios")
    search_fields = ("nombre", "codigo", "facultad")
    list_filter = ("facultad",)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "semestre", "programa")
    search_fields = ("nombre", "codigo")
    list_filter = ("programa", "semestre")


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo_estudiante", "correo", "programa", "fecha_ingreso")
    search_fields = ("nombre", "correo", "codigo_estudiante")
    list_filter = ("programa", "fecha_ingreso")
