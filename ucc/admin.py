from django.contrib import admin
from .models import Programa, Curso, Estudiante, Inscripcion

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'programa', 'creditos')
    list_filter = ('programa',)
    search_fields = ('codigo', 'nombre')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'email')
    search_fields = ('codigo', 'nombre', 'email')

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'curso', 'fecha')
    list_filter = ('curso__programa', 'curso')
    search_fields = ('estudiante__codigo', 'estudiante__nombre', 'curso__codigo', 'curso__nombre')
