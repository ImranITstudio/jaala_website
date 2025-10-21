from django.shortcuts import render
from blogs.models import Blog

def index(request):
    latest_blogs = Blog.objects.all().order_by('-date')[:3]
    return render(request, 'index.html', {'latest_blogs': latest_blogs})
