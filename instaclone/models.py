# import profile
# from tkinter import image_names
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    profile_picture = CloudinaryField('image')
    user =models.CharField(max_length=30)
    name =models.CharField(max_length=50, blank=True)
    bio = models


    def __str__(self):
        return self.user.username


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
    comment = models.TextField()
    # post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.user.name} Post'

    class Meta:
        ordering = ['-created_on']    






