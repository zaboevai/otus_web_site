from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Lesson, Course, Teacher


class IndexPageView(TemplateView):
    template_name = 'online_school/index.html'


class CoursesListView(ListView):
    template_name = 'online_school/courses.html'
    model = Course


class LessonsListView(ListView):
    template_name = 'online_school/lessons.html'
    model = Lesson

class TeachersListView(ListView):
    template_name = 'online_school/teachers.html'
    model = Teacher
