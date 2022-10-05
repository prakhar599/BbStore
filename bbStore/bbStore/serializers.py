from rest_framework import serializers
from blog.models import Blog
from django.contrib.auth.models import User



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['entry','name','tag_line','content','img']
        
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

    
    