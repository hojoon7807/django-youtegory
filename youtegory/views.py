from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404


# Create your views here.
def video_list(request):
    return render(request, 'main.html')


def category_list(request):
    return render(request, 'categoryPage.html')
