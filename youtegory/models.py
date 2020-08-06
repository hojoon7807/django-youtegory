from django.db import models
from django.conf import settings


# Create your models here.

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.video_id
