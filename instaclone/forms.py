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
        exclude = ['author', 'published_date']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
        }  
         

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['author']
        fields ='__all__'    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author', 'created_on', 'post']
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].label = ""          
                    