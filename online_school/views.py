from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'online_school/index.html'


class CoursesPageView(TemplateView):
    template_name = 'online_school/courses.html'


class LessonsPageView(TemplateView):
    template_name = 'online_school/lessons.html'


class TeachersPageView(TemplateView):
    template_name = 'online_school/teachers.html'

