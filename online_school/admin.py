from django.contrib import admin
from .models import Course, TypeCourse, Teacher, Lesson, Student


@admin.register(TypeCourse)
class TypeCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type_fk', 'created')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic')


@admin.register(Lesson)
class CourseLessonsAdmin(admin.ModelAdmin):
    list_display = ('course_fk', 'id', 'title', 'desc', 'date', 'time')


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic')
