from django import forms

from .models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email = forms.EmailField(
        label = "Электронная почта",
        widget = forms.EmailInput(attrs={"class":"form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    
class UserRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'phone',
            'avatar',
        ]
    
    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Пароли не совпадают')
    #     return cd['password2']