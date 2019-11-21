from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):

    username = forms.CharField(label='* Логин', max_length=254)
    first_name = forms.CharField(label='Имя',  required=False, max_length=254)
    last_name = forms.CharField(label='Фамилия', required=False, max_length=254)
    email = forms.EmailField(label='* Адрес электронной почты', max_length=254)

    password1 = forms.CharField(
        label="* Пароль",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="* Подтвердите пароль",
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    # def __init__(self):
    #     super().__init__()
    #     self.password1.label = "Пароль"
        # self.password1.label = 'Пароль'
        # self.password2.label = 'Логин'