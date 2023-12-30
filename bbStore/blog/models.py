from django.db import models
from ckeditor.fields import RichTextField



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
    name = models.CharField(max_length=100)
    mail = models.EmailField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    blog_id = models.AutoField
    entry = models.ForeignKey(Author,related_name='authors',on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    tag_line = models.CharField(max_length = 100)
    content = RichTextField()
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

