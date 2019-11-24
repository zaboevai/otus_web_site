from django.contrib.auth.models import AbstractUser
from django.db import models


class AbstractPeopleNamesMixin(models.Model):
    class Meta:
        abstract = True

    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)


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


class SubscribeEmail(models.Model):
    class Meta:
        ordering = ('id',)

    email = models.EmailField(max_length=255)


class TypeCourse(AbstractDateTimeMixin):
    class Meta:
        ordering = ('id',)

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    patronymic = models.CharField(max_length=255)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, null=True, blank=True, )
    birth_date = models.DateField(null=True, blank=True, )


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.user.patronymic}'


class Course(AbstractTitleDescMixin, AbstractDateTimeMixin):
    class Meta:
        ordering = ('id',)

    created = models.DateTimeField(auto_now_add=True)
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
