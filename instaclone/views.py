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
    comment_form = CommentForm
    return render(request,'instaclone/index.html', {'comment_form': comment_form, "posts":posts, "ctx":ctx})

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
        Profile.objects.filter(id__gt=1)
        
        profile=Profile.objects.get(author= request.user.id)
       
        if form.is_valid():
            avatar=form.cleaned_data['avatar']   
            name=form.cleaned_data['name']  
            bio=form.cleaned_data['bio'] 
            author=request.user            
            profile=Profile(avatar,name,bio,author)
            form.save()

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
    if request.method == 'POST':
        form = CommentForm(request.POST)
       
        if form.is_valid():
            comment = Comment()
            comment.post = Post.objects.get(id=request.POST['post_id'])
            comment.author = request.user
            comment.comment = form.cleaned_data['comment']
                     
            comment.save()
            messages.success(request, 'Comment has been added')

            return redirect ('index')
        else:
            return redirect ('index')



def post(request):
    form = PostForm
    current_user = request.user
    if request.method == 'POST':
        print(request.POST['post'])
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.post = form.cleaned_data['post']
            post.author = current_user
            post.picture = form.cleaned_data['image']
            post.save()
            messages.success(request, 'Posted')

            return redirect ('index')
        else:
            return render(request, 'post/new_post.html', {'form': form})

    else:
        return render(request, 'post/new_post.html', {'form': form})                          







