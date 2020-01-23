from django import forms
from . import models


class HumanForm(forms.ModelForm):
    class Meta:
        model = models.Human
        fields = ['name', 'surname', 'age', 'company', 'salary']
