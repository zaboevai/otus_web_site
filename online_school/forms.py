from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.db import transaction
from django.utils.translation import gettext_lazy as _

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
                  'password2',
                  )

        labels = {'username': _('Логин'),
                  'email': _('Адрес электронной почты'),
                  }

        help_texts = {'username': 'Обязательное. 150 символов максимум. Допустимые символы @/./+/-/_ .',
                      'password1': ' ',
                      'password2': ' '}

    user_roles = ((1, 'Студент'),
                  (2, 'Учитель')
                  )

    user_role = forms.ChoiceField(label='Какую учетную запись вы хотите создать?', choices=user_roles)

    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_("Подтвердите пароль"),
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

        return user


class UserExtendedForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name',
                  'first_name',
                  'patronymic',)

        labels = {'last_name': _('Фамилия'),
                  'first_name': _('Имя'),
                  'patronymic': _('Отчество'), }

    def save(self, commit=True):
        user = self.instance
        user.last_name = self.cleaned_data.get('last_name')
        user.first_name = self.cleaned_data.get('first_name')
        user.patronymic = self.cleaned_data.get('patronymic')
        if commit:
            user.save()

        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone',
                  'birth_date',)

    phone = forms.CharField(label='Телефон', required=False, max_length=20)
    birth_date = forms.DateField(label='Дата рождения',
                                 required=False,
                                 )
