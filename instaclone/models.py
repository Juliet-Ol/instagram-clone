import profile
from tkinter import image_names
from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    name = models.CharField(max_length=30)


class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    profile = models.ForeignKey(User, on_delete= models.CASCADE)
    likes = models.BooleanField()
    comment = models.CharField(max_length=100)


