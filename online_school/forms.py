from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.db import transaction

from online_school.models import Profile, Student, Teacher

User = get_user_model()


class AuthForm(AuthenticationForm):
    username = UsernameField(label='Логин', widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput,
    )


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('user_role',
                  'username',
                  'email',
                  'password1',
                  'password2',)

    username = forms.CharField(label='Логин', max_length=254)
    email = forms.EmailField(label='Адрес электронной почты', max_length=254)

    user_roles = ((1, 'Студент'),
                  (2, 'Учитель')
                  )

    user_role = forms.ChoiceField(label='Какую учетную запись вы хотите создать?', choices=user_roles)

    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput,
        strip=False,
    )

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['user_role'] == '1':
            user.is_student = True
            user.save()
            student = Student.objects.create(user=user)
        else:
            user.is_teacher = True
            user.save()
            teacher = Teacher.objects.create(user=user)

        profile = Profile.objects.create(user=user)

        return user


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name',
                  'last_name',
                  'patronymic',
                  'phone',
                  'birth_date')

    first_name = forms.CharField(label='Имя', required=False, max_length=254)
    last_name = forms.CharField(label='Фамилия', required=False, max_length=254)
    patronymic = forms.CharField(label='Отчество', required=False, max_length=254)
    phone = forms.CharField(label='Телефон', required=False, max_length=20)
    birth_date = forms.DateField(label='Дата рождения',
                                 required=False,
                                 )

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile, is_created = profile.objects.update_or_create(phone=self.phone,
                                                               birth_date=self.birth_date)
