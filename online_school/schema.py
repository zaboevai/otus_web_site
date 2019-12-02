import graphene
from graphene_django import DjangoObjectType

from .models import *


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher


class TypeCourseType(DjangoObjectType):
    class Meta:
        model = TypeCourse


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class Query:
    all_teachers = graphene.List(of_type=TeacherType)
    all_course = graphene.List(of_type=CourseType)
    all_type_course = graphene.List(of_type=TypeCourseType)

    course = graphene.Field(CourseType, id=graphene.Int(), title=graphene.String())

    def resolve_all_teachers(self, info, **kwargs):
        return Teacher.objects.all()

    def resolve_all_course(self, info, **kwargs):
        return Course.objects.all()

    def resolve_course(self, info, **kwargs):
        if kwargs['id']:
            return Course.objects.get(id=kwargs['id'])

    def resolve_all_type_course(self, info, **kwargs):
        return TypeCourse.objects.all()
