# academico/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Programas
    path("programas/", views.lista_programas, name="programa-list"),
    path("programas/<int:pk>/", views.detalle_programa, name="programa-detail"),
    # Cursos
    path("cursos/", views.lista_cursos, name="curso-list"),
    path("cursos/<int:pk>/", views.detalle_curso, name="curso-detail"),
    # Estudiantes
    path("estudiantes/", views.lista_estudiantes, name="estudiante-list"),
    path("estudiantes/<int:pk>/", views.detalle_estudiante, name="estudiante-detail"),
    # Acción de inscripción
    path("estudiantes/<int:estudiante_pk>/inscribir/", views.inscribir_estudiante_en_curso, name="inscripcion-create"),
]
