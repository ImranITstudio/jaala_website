from django.urls import path 

from . import views

urlpatterns = [
    path('', views.blogs_list, name='blogs_list'),
    path('<slug:slug>/', views.blog_page, name='blog_page'),

]