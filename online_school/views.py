from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView

from online_school.forms import UserForm, ProfileForm, AuthForm
from .models import Lesson, Course, Teacher, User, Profile


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


class ContactsListView(TemplateView):
    template_name = 'online_school/contacts.html'


class LoginAuthView(LoginView):
    form_class = AuthForm
    template_name = 'registration/login.html'


class LogoutAuthView(LogoutView):
    template_name = 'registration/logout.html'


class PasswordRessetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'


class RegistrationView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data()

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class ProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/profile.html'
