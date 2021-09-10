
from django.core import validators
from django import forms
from django.forms import widgets
from .models import KeyUser



class StudentRegistration(forms.ModelForm):

    class Meta:
        model = KeyUser
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),

        }

















