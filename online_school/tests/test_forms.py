from datetime import datetime

from django.test import TestCase

from online_school.forms import ProfileForm, User
from online_school.models import Profile


class TestProfileForm(TestCase):

    def test_profile_validation_form(self):
        data = {'phone': '+71234567890',
                'birth_date': '01/01/1990',
                'is_subscribe': True,
                }
        form = ProfileForm(data=data)
        self.assertTrue(form.is_valid())

    def test_profile_save_form(self):
        data = {'phone': '+71234567890',
                'birth_date': '01/01/1990',
                'is_subscribe': True,
                }
        form = ProfileForm(data=data)
        form.full_clean()
        profile=form.save(commit=False)
        self.assertEqual(profile.phone, data.get('phone'))
        self.assertEqual(datetime.strftime(profile.birth_date, '%d/%m/%Y'), data.get('birth_date'))
        self.assertEqual(profile.is_subscribe, data.get('is_subscribe'))
