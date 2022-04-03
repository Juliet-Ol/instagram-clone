from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Image, Profile
from .forms import ImageForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import datetime as dt

# def welcome(request):
#     return HttpResponse('This is an instagram clone')

def index(request): 
    image = Image.objects.all() 
    ctx = {'image':image}
    
    return render(request,'instaclone/index.html', ctx)

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
        
        profile=Profile.objects.get(author= request.user.id)
       
        if form.is_valid():
            profile.avatar=form.cleaned_data['avatar']   
            profile.name=form.cleaned_data['name']  
            profile.bio=form.cleaned_data['bio'] 
            profile.author=request.user            
            
            profile.save()
            messages.success(request, 'Profile has been updated')

            return redirect ('/profile')
        else:
            return render(request, 'profile/edit.html', {'form': form})

    else:
        profile=Profile.objects.get(author= request.user.id)

        return render(request, 'profile/show.html', {'form': form, 'profile':profile})        







