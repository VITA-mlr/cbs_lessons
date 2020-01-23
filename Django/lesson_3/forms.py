from django import forms
from . import models
from django.core.validators import URLValidator, ValidationError


class RespondForm(forms.ModelForm):
    class Meta:
        model = models.Respond
        fields = ['login', 'respond']
