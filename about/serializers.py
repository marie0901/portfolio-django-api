from rest_framework import serializers

from . import models


class AboutSlideSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'type',
            'id',
            'image_url',
            'title',
            'order'
        )
        model = models.AboutSlide

    def get_type(self, slide):
        return 'about-slide'

    # return slide's image url if available
    def get_image_url(self, slide):
        return slide.image.url if slide.image else ''
