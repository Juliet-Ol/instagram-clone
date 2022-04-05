# import profile
# from tkinter import image_names
from cProfile import label
import datetime as dt
from email.policy import default
# from email.mime import image
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone




# from instaclone.forms import PostForm


class Profile(models.Model):
    avatar = models.ImageField(upload_to='image', null=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    name =models.CharField(max_length=50, blank=True)
    bio = models.TextField(null=True)

    
    def __str__(self):
        return self.use

    def save_profile(self):
        self.save()

    def save_profile(self):
        self.delete()        


class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    profile = models.ForeignKey(User, on_delete= models.CASCADE)
    likes = models.BooleanField()
   
    comment = models.CharField(max_length=100)
    
    class Meta:
        ordering =['-likes']

    def __str__(self):
        return self.image_name       

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()    


    
class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name  

class Title(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name  




class Post (models.Model):
    title = models.CharField(max_length=20)
    post = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='image', null=True)

    class Meta:
        ordering = ['-published_date']  

    @classmethod
    def display(cls):
        posts = cls.objects.all()
        return posts

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()       

class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    comment = models.TextField(null=True)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment: {} by {}'.format(self.comment, self.author.username)  


    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete() 







