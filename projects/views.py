from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import permissions

from . import models, serializers
from tags.serializers import TagSerializer
from learning.serializers import CourseSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    # return only published items
    queryset = models.Project.visible.all()
    serializer_class = serializers.ProjectSerializer

    def retrieve(self, request, pk=None):
        queryset = self.queryset

        try: # retrieve project by primary key
            pk = int(pk)
            project = get_object_or_404(queryset, pk=pk)
            serializer = self.get_serializer(project)
            return Response(serializer.data)

        except: # retrieve project by title
            project = get_object_or_404(queryset.filter(url_name=pk))
            serializer = self.get_serializer(project)
            return Response(serializer.data)

    # detail route to return project tags
    # .../projects/[project_id]/tags
    @detail_route(methods=['get'])
    def tags(self, request, pk=None):
        project = self.get_object()
        serializer = TagSerializer(project.tags, many=True)
        return Response(serializer.data)

    # detail route to return project technologies
    # .../projects/[project_id]/technologies
    @detail_route(methods=['get'])
    def technologies(self, request, pk=None):
        project = self.get_object()
        serializer = serializers.TechnologySerializer(project.technologies, many=True)
        return Response(serializer.data)

    # detail route to return course info for a project
    # .../projects/[project_id]/course
    @detail_route(methods=['get'])
    def course(self, request, pk=None):
        project = self.get_object()
        serializer = CourseSerializer(project.course, many=False)
        return Response(serializer.data)

    # list route to return latest projects
    # .../projects/latest
    @list_route()
    def latest(self, request):
        latest_projects = models.Project.visible.all()[:3]
        serializer = self.get_serializer(latest_projects, many=True)
        return Response(serializer.data)