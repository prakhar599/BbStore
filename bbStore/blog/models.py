from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(blank=True)
    tagline = models.CharField(max_length=255, blank=True)
    twitter_profile = models.URLField(max_length=255, blank=True)
    instagram_profile = models.URLField(max_length=255, blank=True)
    github = models.URLField(max_length=255, blank=True)
    stackoverflow = models.URLField(max_length=255, blank=True)
    personal_website = models.URLField(max_length=255, blank=True)
    linkedin_channel = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    blog_id = models.AutoField
    entry = models.ForeignKey(Author,related_name='authors',on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    tag_line = models.CharField(max_length = 100)
    content = RichTextField()
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

