from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, ListView, CreateView

from online_school import tasks
from online_school.forms import UserForm, ProfileForm, AuthForm, UserExtendedForm
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

    def get(self, request, *args, **kwargs):
        user_form = UserExtendedForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request, *args, **kwargs):
        user_form = UserExtendedForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            try:
                if profile_form.cleaned_data['is_subscribe']:
                    tasks.send_subscribe_email.delay(request.user.email)
                else:
                    tasks.send_unsubscribe_email.delay(request.user.email)
            except BaseException as exc:
                messages.success(request, _(f'Ошибка отправки уведомления: {exc}'))

            messages.success(request, _('Профиль был успешно обновлен !'))
            return render(request, self.template_name, {
                'user_form': user_form,
                'profile_form': profile_form
            })
        else:
            messages.error(request, _('Please correct the error below.'))

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })
