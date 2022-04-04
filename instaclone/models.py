# import profile
# from tkinter import image_names
import datetime as dt
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

    def save_profile(self):
        self.save()


    def __str__(self):
        return self.use


class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    profile = models.ForeignKey(User, on_delete= models.CASCADE)
    likes = models.BooleanField()
   
    comment = models.CharField(max_length=100)
    
    class Meta:
        ordering =['-likes']

       

class Comment(models.Model):
    # post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80, default=True)
    comment = models.TextField(default=True)
    # email = models.EmailField()
    # body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user.username}Post'

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)  



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
    image = models.ImageField( blank=True, upload_to='images')

    class Meta:
        ordering = ['-published_date']        






