from django.contrib import admin

from .models import Course, TypeCourse, Lesson, Teacher, Student, StudentsGroup, Profile


@admin.register(TypeCourse)
class TypeCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'type')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Lesson)
class CourseLessonsAdmin(admin.ModelAdmin):
    list_display = ('course', 'id', 'title', 'desc', 'date', 'time', 'created')


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_group')


@admin.register(StudentsGroup)
class StudentsGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'birth_date',)
