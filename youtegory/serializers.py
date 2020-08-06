from rest_framework import serializers
from .models import Category, Video

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'category_name')


class VideoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Video
        fields = ('category', 'video_id', 'title')