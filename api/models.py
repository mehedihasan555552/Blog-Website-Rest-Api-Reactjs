from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class BlogTags(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    tags = models.ManyToManyField(BlogTags, related_name='blog_tags')
    title = models.CharField(max_length=200)
    image = models.ImageField(default='hello.jpg',blank=True,null=True)
    author = models.ForeignKey(User,related_name='blog_author',on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ('-created_at',)


    def __str__(self):
        return self.title

class BlogComments(models.Model):
    blog=models.ForeignKey(Blog,related_name='blog_comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=255,default='Annoymous')
    ip = models.CharField(max_length=255,blank=True,null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class meta:
        ordering = ('-created_at')

    def __str__(self):
        return self.comment
