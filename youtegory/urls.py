from django.urls import path, include
from youtegory import views

urlpatterns = [
    path('', views.main, name='main'),
    path('categorylist', views.category_list, name='category_list'),
    path('videos', views.video_list, name='video_list'),
    path('categories', views.category_new, name='category_new'),
    path('categories/<int:category_id>/videos', views.video_new, name='video_new'),
]   