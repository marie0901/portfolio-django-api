from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import permissions

from . import models, serializers
from tags.serializers import TagSerializer
from projects.models import Project
from projects.serializers import ProjectSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def retrieve(self, request, pk=None):
        queryset = self.queryset

        try: # retrieve book by primary key
            pk = int(pk)
            book = get_object_or_404(queryset, pk=pk)
            serializer = self.get_serializer(book)
            return Response(serializer.data)

        except: # retrieve book by name
            book = get_object_or_404(queryset.filter(url_name=pk))
            serializer = self.get_serializer(book)
            return Response(serializer.data)

    # detail route to return book tags
    # .../learning/books/[book_id]/tags
    @detail_route(methods=['get'])
    def tags(self, request, pk=None):
        book = self.get_object()
        serializer = TagSerializer(book.tags, many=True)
        return Response(serializer.data)


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    def retrieve(self, request, pk=None):
        queryset = self.queryset

        try: # retrieve course by primary key
            pk = int(pk)
            course = get_object_or_404(queryset, pk=pk)
            serializer = self.get_serializer(course)
            return Response(serializer.data)

        except: # retrieve course by title
            course = get_object_or_404(queryset.filter(url_title=pk))
            serializer = self.get_serializer(course)
            return Response(serializer.data)

    # detail route to return course projects
    # .../learning/courses/[course_id]/projects
    @detail_route(methods=['get'])
    def projects(self, request, pk=None):
        course = self.get_object()
        course_projects = Project.objects.filter(course_id=course.id)
        serializer = ProjectSerializer(course_projects, many=True)
        return Response(serializer.data)

    # detail route to return course tags
    # .../learning/courses/[course_id]/tags
    @detail_route(methods=['get'])
    def tags(self, request, pk=None):
        course = self.get_object()
        serializer = TagSerializer(course.tags, many=True)
        return Response(serializer.data)

    # detail route to return school info for a course
    # .../learning/courses/[course_id]/school
    @detail_route(methods=['get'])
    def school(self, request, pk=None):
        course = self.get_object()
        school = course.school
        serializer = serializers.SchoolSerializer(school, many=False)
        return Response(serializer.data)

    # list route to return current courses
    # .../learning/courses/current
    @list_route(methods=['get'])
    def current(self, request):
        current_courses = models.Course.objects.filter(current=True)
        serializer = serializers.CourseSerializer(current_courses, many=True)
        return Response(serializer.data)

class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer

    def retrieve(self, request, pk=None):
        queryset = self.queryset

        try: # retrieve school by primary key
            pk = int(pk)
            school = get_object_or_404(queryset, pk=pk)
            serializer = self.get_serializer(school)
            return Response(serializer.data)

        except: # retrieve school by name
            school = get_object_or_404(queryset.filter(url_name=pk))
            serializer = self.get_serializer(school)
            return Response(serializer.data)

    # detail route to return school tags
    # .../learning/schools/[school_id]/tags
    @detail_route(methods=['get'])
    def tags(self, request, pk=None):
        school = self.get_object()
        serializer = TagSerializer(school.tags, many=True)
        return Response(serializer.data)

    # detail route to return all courses of school
    # .../learning/schools/[school_id]/courses
    @detail_route(methods=['get'])
    def courses(self, request, pk=None):
        school = self.get_object()
        courses = models.Course.objects.filter(school_id=school.id)
        serializer = serializers.CourseSerializer(courses, many=True)
        return Response(serializer.data)


class QuoteViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer

    # detail route to return quote tags
    # .../learning/quotes/[quote_id]/tags
    @detail_route(methods=['get'])
    def tags(self, request, pk=None):
        quote = self.get_object()
        serializer = TagSerializer(quote.tags, many=True)
        return Response(serializer.data)
