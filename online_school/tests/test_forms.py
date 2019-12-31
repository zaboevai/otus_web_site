from datetime import datetime

from django.test import TestCase

from online_school.forms import ProfileForm, UserExtendedForm, UserForm


class TestProfileForm(TestCase):
    data = {'phone': '+71234567890',
            'birth_date': '01/01/1990',
            'is_subscribe': True,
            }

    def test_profile_validation_form(self):
        form = ProfileForm(data=TestProfileForm.data)
        self.assertTrue(form.is_valid())

    def test_profile_save_form(self):
        form = ProfileForm(data=TestProfileForm.data)
        form.full_clean()
        profile = form.save(commit=False)
        self.assertEqual(profile.phone, TestProfileForm.data.get('phone'))
        self.assertEqual(datetime.strftime(profile.birth_date, '%d/%m/%Y'), TestProfileForm.data.get('birth_date'))
        self.assertEqual(profile.is_subscribe, TestProfileForm.data.get('is_subscribe'))


class TestUserExtendedForm(TestCase):
    data = {'last_name': 'Иванов',
            'first_name': 'Иван',
            'patronymic': 'Иванович'
            }

    def test_user_extended_validation_form(self):
        form = UserExtendedForm(data=TestUserExtendedForm.data)
        self.assertTrue(form.is_valid())

    def test_user_extended_save_form(self):
        form = UserExtendedForm(data=TestUserExtendedForm.data)
        form.full_clean()
        user = form.save(commit=False)
        self.assertEqual(user.last_name, TestUserExtendedForm.data.get('last_name'))
        self.assertEqual(user.first_name, TestUserExtendedForm.data.get('first_name'))
        self.assertEqual(user.patronymic, TestUserExtendedForm.data.get('patronymic'))


class TestUserForm(TestCase):
    data = {'user_role': 1,
            'username': 'qwerty',
            'email': '1@1.ru',
            'password1': 'PoiuY321',
            'password2': 'PoiuY321'
            }

    def test_user_validation_form(self):
        form = UserForm(data=TestUserForm.data)
        self.assertTrue(form.is_valid())

    def test_user_save_form(self):
        form = UserForm(data=TestUserForm.data)
        form.full_clean()
        user = form.save(commit=False)
        self.assertEqual(user.is_student, TestUserForm.data.get('user_role'))
        self.assertEqual(user.username, TestUserForm.data.get('username'))
        self.assertEqual(user.email, TestUserForm.data.get('email'))