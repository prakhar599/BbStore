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

class UserFollowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")

    class Meta:
        # Add a unique constraint to ensure each user can follow another user only once
        unique_together = ['user', 'following_user']
        
    def __str__(self):
        return f"{self.user.username} follows {self.following_user.username}"

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
    
class EBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to='ebook_covers/', null=True, blank=True)
    language = models.CharField(max_length=50)
    pages = models.PositiveIntegerField()
    publisher = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)
    average_rating = models.FloatField(default=0.0)
    total_ratings = models.PositiveIntegerField(default=0)
    file = models.FileField(upload_to='ebooks/')
    file_format = models.CharField(max_length=10, choices=[('PDF', 'PDF'), ('EPUB', 'EPUB'), ('MOBI', 'MOBI')])
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


