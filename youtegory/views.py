from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Video
from .serializers import CategorySerializer, VideoSerializer

# Create your views here.
def main(request):
    return render(request, 'main.html')


def category_list(request):
    return render(request, 'categoryPage.html')


@api_view(['GET'])
def video_list(request):
    videolists = Video.objects.all()
    serializer = VideoSerializer(videolists, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def category_new(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST','PUT','DELETE'])
def video_new(request, category_id):
    if request.method == 'POST':
        print(request.data)
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

