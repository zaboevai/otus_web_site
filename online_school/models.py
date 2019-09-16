from django.db import models


class TypeCourse(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):

    name = models.CharField(max_length=255)
    type = models.ForeignKey('TypeCourse', null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.name} ({self.type})'


class Teacher(models.Model):

    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class Student(models.Model):

    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class Lesson(models.Model):

    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    type_course = models.ForeignKey('Course', null=True, blank=True, on_delete=models.CASCADE)

    teacher = models.ForeignKey('Teacher', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField()
    time = models.TimeField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.teacher})'


class CourseList(models.Model):

    course_id = models.ForeignKey('Course', null=True, blank=True, on_delete=models.SET_NULL)
    student_id = models.ForeignKey('Student', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.course_id}'
