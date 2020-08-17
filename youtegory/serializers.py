from rest_framework import serializers
from .models import Category, Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('category_id', 'category_name', 'videos',)


