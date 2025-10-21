from django.shortcuts import render
from .models import Blog
# Create your views here.
def blogs_list(request):
    blogs = Blog.objects.all().order_by('-date')
    context = {
        'blogs' : blogs
    }
    return render(request, 'blogs/blogs_list.html', context)