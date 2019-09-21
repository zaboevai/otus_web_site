from django.db import models


class TypeCourse(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):

    class Meta:
        ordering = ('id',)

    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    course_fk = models.ManyToManyField('Course')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class Student(models.Model):

    class Meta:
        ordering = ('id',)

    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    e_mail = models.CharField(max_length=255)
    group_fk = models.ForeignKey('StudentsGroup', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class StudentsGroup(models.Model):

    class Meta:
        ordering = ('course_fk','id')

    name = models.CharField(max_length=255)
    course_fk = models.ForeignKey('Course', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} {self.course_fk}'


class Course(models.Model):

    class Meta:
        ordering = ('id',)

    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    type_fk = models.ForeignKey('TypeCourse', null=True, blank=True, on_delete=models.SET_NULL)
    teacher_fk = models.ManyToManyField('Teacher')

    def __str__(self):
        return f' {self.name} ({self.type_fk})'


class Lesson(models.Model):

    class Meta:
        ordering = ('course_fk', 'id')

    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)

    course_fk = models.ForeignKey('Course', null=True, blank=True, on_delete=models.CASCADE)
    teacher_fk = models.ForeignKey('Teacher', null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} '
