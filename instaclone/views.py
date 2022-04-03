from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Image
from .forms import ImageForm
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

            # return redirect (request, 'registration/registration_form.html', {'form': form})
        # else:
        #     return render(request, 'registration/registration_form.html', {'form': form})

    # else:
    return render(request, 'registration/registration_form.html', {'form': form})




