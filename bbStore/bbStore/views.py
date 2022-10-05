from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.conf import settings
from rest_framework import viewsets
from django.contrib.auth.models import User
from blog.models import Blog
from .serializers import UserSerializer,BlogSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer       
  
    
