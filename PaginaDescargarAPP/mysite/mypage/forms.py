from django import forms
from .models import Profesor

class Loginform(forms.ModelForm):
    class Meta:
        model = Profesor