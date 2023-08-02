from django import forms
from .models import CLAP

class CLAPCreateForm(forms.ModelForm):
    class Meta:
        model=CLAP
        fields=('full_name', 'address')