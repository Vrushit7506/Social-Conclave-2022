from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .models import Blog
import json
app_name = "core"


# def jsonitems(request):
#     blogs = serializers.serialize("json", Blog.objects.all().order_by('time'))
#     blogs = json.loads(blogs)
#     return JsonResponse(blogs, safe=False)


# def home(request):
#     return render(request, 'blogs/bloghome.html', {'blogs': [1, 2, 3, 4, 5]})


# def blogview(request, blog):
#     blogs = Blog.objects.filter(slug__icontains=blog).first()
#     return render(request, 'blogs/blog.html', {'blog': blogs})

def allblog(request):
    allblogs = Blog.objects.all()
    return render(request, 'blogs/allblogs.html', {'allblogs': allblogs})


def eachblog(request, blogslug):
    return render(request, f'blogs/{blogslug}.html')
