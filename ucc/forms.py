from django import forms
from django.core.exceptions import ValidationError
from .models import Inscripcion, Estudiante, Curso

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso']

    def clean(self):
        cleaned = super().clean()
        est = cleaned.get('estudiante')
        cur = cleaned.get('curso')
        if est and cur and Inscripcion.objects.filter(estudiante=est, curso=cur).exists():
            raise ValidationError("Este estudiante ya está inscrito en ese curso.")
        return cleaned

# Versión conveniente para inscribir desde la vista de Estudiante (oculta el estudiante)
class InscripcionDesdeEstudianteForm(InscripcionForm):
    estudiante = forms.ModelChoiceField(queryset=Estudiante.objects.all(), widget=forms.HiddenInput())
    curso = forms.ModelChoiceField(queryset=Curso.objects.all())
