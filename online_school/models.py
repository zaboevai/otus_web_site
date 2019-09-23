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


class TypeCourse(AbstractDateTimeMixin):
    class Meta:
        ordering = ('id',)

    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Teacher(AbstractPeopleNamesMixin, AbstractDateTimeMixin):
    class Meta:
        ordering = ('id',)

    courses = models.ManyToManyField('Course', related_name='Teacher', through='TeacherCourse')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class TeacherCourse(AbstractDateTimeMixin):
    class Meta:
        unique_together = (('teacher', 'course',),)

    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher_id} {self.course_id}'


class Student(AbstractPeopleNamesMixin, AbstractDateTimeMixin):
    class Meta:
        ordering = ('id',)

    e_mail = models.CharField(max_length=255)
    group = models.ForeignKey('StudentsGroup', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class StudentsGroup(AbstractDateTimeMixin):
    class Meta:
        ordering = ('course', 'id')

    name = models.CharField(max_length=255)
    course = models.ForeignKey('Course', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} {self.course}'


class Course(AbstractTitleDescMixin, AbstractDateTimeMixin):
    class Meta:
        ordering = ('id',)

    created = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey('TypeCourse', null=True, blank=True, on_delete=models.SET_NULL)
    teachers = models.ManyToManyField('Teacher', related_name='Course', through='TeacherCourse')

    def __str__(self):
        return f' {self.title} ({self.type})'


class Lesson(AbstractTitleDescMixin, AbstractDateTimeMixin):
    class Meta:
        ordering = ('course', 'id')

    course = models.ForeignKey('Course', null=True, blank=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.title} '
