from django.urls import path, include
from youtegory import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('categorylist', views.category_list, name='category_list')
]