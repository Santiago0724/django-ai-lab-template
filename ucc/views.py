# ucc/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Programa, Curso, Estudiante, Inscripcion

def home(request):
    return render(request, "ucc/home.html", {})

# --- Programas ---
def lista_programas(request):
    programas = Programa.objects.all().order_by("nombre")
    return render(request, "ucc/programa_list.html", {"programas": programas})

def detalle_programa(request, pk):
    programa = get_object_or_404(
        Programa.objects.prefetch_related("cursos"),
        pk=pk
    )
    return render(request, "ucc/programa_detail.html", {"programa": programa})

# --- Cursos ---
def lista_cursos(request):
    cursos = (
        Curso.objects
        .select_related("programa")
        .all()
        .order_by("codigo")
    )
    return render(request, "ucc/curso_list.html", {"cursos": cursos})

def detalle_curso(request, pk):
    curso = get_object_or_404(
        Curso.objects.select_related("programa").prefetch_related("estudiantes"),
        pk=pk
    )
    return render(request, "ucc/curso_detail.html", {"curso": curso})

# --- Estudiantes ---
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all().order_by("codigo")
    return render(request, "ucc/estudiante_list.html", {"estudiantes": estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    # cursos del estudiante (M2M via Inscripcion)
    cursos = (
        estudiante.cursos
        .select_related("programa")
        .all()
        .order_by("codigo")
    )
    return render(
        request,
        "ucc/estudiante_detail.html",
        {"estudiante": estudiante, "cursos": cursos}
    )

# --- Acción de inscribir (opcional, mismo estilo funcional) ---
def inscribir_estudiante_en_curso(request, estudiante_pk):
    if request.method != "POST":
        return redirect("estudiante-detail", pk=estudiante_pk)

    estudiante = get_object_or_404(Estudiante, pk=estudiante_pk)
    curso_id = request.POST.get("curso_id")

    if not curso_id:
        messages.error(request, "Debes seleccionar un curso.")
        return redirect("estudiante-detail", pk=estudiante.pk)

    curso = get_object_or_404(Curso, pk=curso_id)

    # Evitar duplicado (UniqueConstraint en Inscripcion lo garantiza; igual lo verificamos aquí)
    existe = Inscripcion.objects.filter(estudiante=estudiante, curso=curso).exists()
    if existe:
        messages.warning(request, "El estudiante ya está inscrito en ese curso.")
        return redirect("estudiante-detail", pk=estudiante.pk)

    Inscripcion.objects.create(estudiante=estudiante, curso=curso)
    messages.success(request, f"{estudiante.nombre} inscrito en {curso.codigo} - {curso.nombre}.")
    return redirect("estudiante-detail", pk=estudiante.pk)
