# from dataclasses import fields
from django import forms
from .models import Image, Profile, Post, Comment

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['bio', 'pub_date']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
        }   

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields ='__all__'     
                    