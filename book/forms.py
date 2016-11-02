from django.forms import ModelForm
from django import forms
from book.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address']


class LoginForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

