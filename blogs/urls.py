from django.urls import path 

from . import views

urlpatterns = [
    path('', views.blogs_list, name='blogs_list'),
]