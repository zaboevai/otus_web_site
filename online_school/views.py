from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Lesson, Course, Teacher
from .serializers import CourseSerializer, UserAuthSerializer, UserLoginSerializer


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


class LoginListView(ListView):
    template_name = 'online_school/login.html'
    model = Teacher


class RegisterListView(ListView):
    template_name = 'online_school/register.html'
    model = Teacher



class AuthApiView(APIView):

    def get(self, request):
        serializer = UserAuthSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(APIView):

    def get(self, request):
        serializer = UserLoginSerializer()
        return Response(serializer.data)

    def post(self, request):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)


class CourseListApiView(APIView):

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class CourseListDetailApiView(APIView):

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(instance=course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        data = serializer.data
        course.delete()
        return Response(data, status=status.HTTP_200_OK)
