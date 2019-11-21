from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from online_school.forms import RegistrationForm
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


class ContactsListView(ListView):
    template_name = 'online_school/contacts.html'
    model = Teacher


class LoginAuthView(LoginView):
    template_name = 'registration/login.html'


# class RegisterAuthView(LoginView):
#     template_name = 'registration/register.html'


class LogoutAuthView(LogoutView):
    template_name = 'registration/logout.html'


class ProfileAuthView(TemplateView):
    template_name = 'registration/profile.html'


class PasswordRessetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'


def registration(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
        return redirect('/')
    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})


