from django import forms
from .models import *


class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'