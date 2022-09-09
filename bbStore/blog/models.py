from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    
    def __str__(self):
        return self.name    
    

class Blog(models.Model):
    blog_id = models.AutoField
    entry = models.ForeignKey(Author,related_name='authors',on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    tag_line = models.CharField(max_length = 32)
    content = models.TextField()
    img = models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.name
    
    