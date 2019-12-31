import datetime

from django.test import TestCase

from online_school.models import Course, TypeCourse, User, Profile


class TestAbstractTitleDescMixin(TestCase):

    @classmethod
    def setUpTestData(cls):
        Course.objects.create(title='Курс', desc='Описание')

    def test_title_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        course = Course.objects.get(id=1)
        length = course._meta.get_field('title').max_length
        self.assertEqual(length, 255)

    def test_desc_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('desc').verbose_name
        self.assertEqual(field_label, 'desc')

    def test_desc_max_length(self):
        course = Course.objects.get(id=1)
        length = course._meta.get_field('desc').max_length
        self.assertEqual(length, 255)


class TestTypeCourse(TestCase):

    @classmethod
    def setUp(cls):
        TypeCourse.objects.create(name='Программирование')

    def test_name_label(self):
        type_course = TypeCourse.objects.get(id=1)
        field_label = type_course._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        type_course = TypeCourse.objects.get(id=1)
        length = type_course._meta.get_field('name').max_length
        self.assertEqual(length, 50)


class TestUser(TestCase):

    @classmethod
    def setUp(cls):
        User.objects.create_user('user', '1@1.mail.ru', 'qwerty123')

    def test_user_email_label(self):
        user = User.objects.get(id=1)
        email_label = user._meta.get_field('email').verbose_name
        self.assertEqual(email_label, 'email address')

    def test_user_email_max_length(self):
        user = User.objects.get(id=1)
        length = user._meta.get_field('email').max_length
        self.assertEqual(length, 254)

    def test_user_patronymic_label(self):
        user = User.objects.get(id=1)
        patronymic_label = user._meta.get_field('patronymic').verbose_name
        self.assertEqual(patronymic_label, 'patronymic')

    def test_user_patronymic_max_length(self):
        user = User.objects.get(id=1)
        length = user._meta.get_field('patronymic').max_length
        self.assertEqual(length, 255)

    def test_user_is_teacher_label(self):
        user = User.objects.get(id=1)
        is_teacher_label = user._meta.get_field('is_teacher').verbose_name
        self.assertEqual(is_teacher_label, 'is teacher')

    def test_user_is_teacher_default(self):
        user = User.objects.get(id=1)
        is_teacher = user._meta.get_field('is_teacher').default
        self.assertEqual(is_teacher, False)

    def test_user_is_student_label(self):
        user = User.objects.get(id=1)
        is_student_label = user._meta.get_field('is_student').verbose_name
        self.assertEqual(is_student_label, 'is student')

    def test_user_is_student_default(self):
        user = User.objects.get(id=1)
        is_student = user._meta.get_field('is_student').default
        self.assertEqual(is_student, False)


class TestProfile(TestCase):

    @classmethod
    def setUp(cls):
        user = User.objects.create_user('testuser', '1@1.mail.ru', 'qwerty123')
        # user = User.objects.get(id=1)
        Profile.objects.update(user=user, phone='+71234561212', birth_date=datetime.date(1990, 1, 1), is_subscribe=True)

    def test_profile_phone_label(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(user=user)
        phone_label = profile._meta.get_field('phone').verbose_name
        self.assertEqual(phone_label, 'phone')

    def test_profile_phone_max_length(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(user=user)

        length = profile._meta.get_field('phone').max_length
        self.assertEqual(length, 20)

    def test_profile_phone_null_param(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(user=user)

        is_null = profile._meta.get_field('phone').null
        self.assertEqual(is_null, True)

    def test_profile_phone_blank_param(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(user=user)

        is_blank = profile._meta.get_field('phone').blank
        self.assertEqual(is_blank, True)

    def test_profile_birth_date_null_param(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(user=user)

        is_null = profile._meta.get_field('birth_date').null
        self.assertEqual(is_null, True)

    def test_profile_birth_date_blank_param(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(user=user)

        is_blank = profile._meta.get_field('birth_date').blank
        self.assertEqual(is_blank, True)

    def test_profile_is_subscribe_default(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(user=user)

        default = profile._meta.get_field('is_subscribe').default
        self.assertEqual(default, False)
