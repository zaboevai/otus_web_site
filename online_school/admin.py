from django.contrib import admin
from .models import * #Course, TypeCourse, Teacher, Lesson, Student, StudentsGroup


@admin.register(SubscribeEmail)
class SubscribeEmailAdmin(admin.ModelAdmin):
    list_display = ('email',)

@admin.register(TypeCourse)
class TypeCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'type', 'display_teacher')

    def display_teacher(self, obj):
        teachers = obj.teachers.values_list('last_name', 'first_name', 'patronymic')
        return '; '.join([' '.join(teacher) for teacher in teachers])


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic')


@admin.register(Lesson)
class CourseLessonsAdmin(admin.ModelAdmin):
    list_display = ('course', 'id', 'title', 'desc', 'date', 'time', 'created')


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic', 'e_mail', 'group')


@admin.register(StudentsGroup)
class StudentsGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course')
