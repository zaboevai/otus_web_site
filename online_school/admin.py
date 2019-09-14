from django.contrib import admin
from .models import Course, TypeCourse, Teacher, Lesson, Student, CourseList


@admin.register(TypeCourse)
class TypeCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic')


@admin.register(Lesson)
class CourseLessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'teacher', 'date', 'time')


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic')


@admin.register(CourseList)
class CourseListAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_id', 'student_id')
