from django.shortcuts import render
from blogs.models import Blog

# Create your views here.


def home(request):
    allblogs = Blog.objects.all()
    return render(request, 'main/index.html', {'allblogs': allblogs})


def ayushya(request):
    return render(request, 'main/blogs.html')
