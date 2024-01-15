from django.urls import path
from . import views
from .views import post_list

urlpatterns = [
  
    path('', views.index, name= "index"),
    path('posts/', views.post_list, name='post_list'),
    path('post/',  views.post_create, name= "post_create"),
    
]
