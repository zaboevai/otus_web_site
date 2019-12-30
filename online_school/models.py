from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class AbstractTitleDescMixin(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)


class AbstractDateTimeMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class TypeCourse(AbstractDateTimeMixin):
    class Meta:
        ordering = ('id',)

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class User(AbstractUser):
    email = models.EmailField(_('email address'))
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    patronymic = models.CharField(max_length=255, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, null=True, blank=True, )
    birth_date = models.DateField(null=True, blank=True)
    is_subscribe = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user} {self.user.last_name} {self.user.first_name} {self.user.patronymic}'


class Course(AbstractTitleDescMixin, AbstractDateTimeMixin):
    class Meta:
        ordering = ('id',)

    type = models.ForeignKey(TypeCourse, null=True, blank=True, on_delete=models.SET_NULL)
    teachers = models.ManyToManyField(Teacher, related_name='Course')

    def __str__(self):
        return f' {self.title} ({self.type})'


class StudentsGroup(AbstractDateTimeMixin):
    class Meta:
        ordering = ('course', 'id')

    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} {self.course}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_group = models.ForeignKey(StudentsGroup, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.user.patronymic}'


class Lesson(AbstractTitleDescMixin, AbstractDateTimeMixin):
    class Meta:
        ordering = ('course', 'id')

    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE, related_name='Course')
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE)
    students_group = models.ForeignKey(StudentsGroup, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.title}'
