from django import forms
from django.db.models.base import Model

from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"