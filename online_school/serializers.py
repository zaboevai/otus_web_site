from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = 'id', 'name', 'desc'

    name = serializers.CharField(required=False)
    desc = serializers.CharField(required=False)


class UserAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'groups')
        # exclude = ('password', 'groups', 'last_login')

    # username = serializers.CharField(required=True)
    # password = serializers.CharField(required=False)
    groups = serializers.CharField(required=False, default='students')
    # email_address = serializers.CharField(required=True)


