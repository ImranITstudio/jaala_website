from django.db import models

# Create your models here.
class Blog(models.Model):
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200)
    content = models.TextField()
    banner_image = models.ImageField(upload_to='blog_banners/', blank=True, default='fallback.png')
    thumbnail_image = models.ImageField(upload_to='blog_thumbnails/', blank=True, default='fallback_thumb.png')
    read_time = models.IntegerField(blank=True, default=5)  # in minutes

    def __str__(self):
        return self.title