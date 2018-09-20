from rest_framework import viewsets
from rest_framework import permissions

from . import models, serializers


class AboutSlideViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    # return only published items
    queryset = models.AboutSlide.visible.all()
    serializer_class = serializers.AboutSlideSerializer
