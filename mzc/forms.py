from django import forms
from .models import Faculty

class FacultyForm(forms.Modelform):
    class Meta:
        fields='__all__'