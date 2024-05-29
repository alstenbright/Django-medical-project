from django import forms
from .models import Customer
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
            model = Customer
            fields = ['username', 'password', 'confirm_password']