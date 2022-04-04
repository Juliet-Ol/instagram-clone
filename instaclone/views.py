from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Image, Profile, Comment, Post
from .forms import CommentForm, ImageForm, ProfileForm, PostForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import datetime as dt

# def welcome(request):
#     return HttpResponse('This is an instagram clone')

def index(request): 
    image = Image.objects.all() 
    ctx = {'image':image}
    posts = Post.display()
    return render(request,'instaclone/index.html', {"posts":posts, "ctx":ctx})

def loadImage(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')


    form = ImageForm()
    ctx = {'form':form}
    return render(request, 'instaclone/load.html')

# User registration 


def register(request):
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been registered')

            return redirect ('/accounts/login')
        else:
            return render(request, 'registration/registration_form.html', {'form': form})

    else:
        return render(request, 'registration/registration_form.html', {'form': form})
        

def editProfile(request):
    form = ProfileForm(initial={'name':request.user.username, 'bio':'test'})

   
    return render(request, 'profile/edit.html', {'form': form})      


def profile(request):
    form = ProfileForm

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        # Profile.objects.filter(id__gt=1)
        
        # profile=Profile.objects.get(author= request.user.id)
       
        if form.is_valid():
            profile.avatar=form.cleaned_data['avatar']   
            profile.name=form.cleaned_data['name']  
            profile.bio=form.cleaned_data['bio'] 
            profile.author=request.user            
            
            profile.save()

            profile=Profile.objects.get(author= request.user.id)
            messages.success(request, 'Profile has been updated')

            return redirect ('/profile')
        else:
            return render(request, 'profile/edit.html', {'form': form})

    else:
        profile=Profile.objects.get(author= request.user)

        return render(request, 'profile/show.html', {'form': form, 'profile':profile})    



def editComment(request):
    form = CommentForm(initial={'name':request.user.username, 'comment':'test'})

   
    return render(request, 'post/comment.html', {'form': form})      


def comment(request):
    form = CommentForm

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
       
        
        comment=Comment.objects.get(author= request.user.id)
       
        if form.is_valid():
            comment = CommentForm.save(commit=False)
                     
            
            profile.save()
            messages.success(request, 'Comment has been added')

            return redirect ('/comment')
        else:
            return render(request, 'post/comment.html', {'form': form})

    else:
        comment=Comment.objects.get(author= request.user.id)

        return render(request, 'profile/show.html', {'form': form, 'comment':comment})     



def post(request):
    form = PostForm
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Posted')

            return redirect ('index')
        else:
            return render(request, 'post/new_post.html', {'form': form})

    else:
        return render(request, 'post/new_post.html', {'form': form})                          







