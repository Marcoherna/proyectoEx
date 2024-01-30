from django import forms
from .models import Trabajador
from django.forms import ModelForm

class TrabajadorForm(ModelForm):
    class Meta:
        model  = Trabajador
        fields = "__all__"

