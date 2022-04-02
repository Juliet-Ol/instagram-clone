from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Image
from .forms import ImageForm
from django.contrib.auth.forms import UserCreationForm


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


def register(request):
    form = UserCreationForm(request.POST or None)
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect ('instaclone/index.html')
    #     else:
    #         return render(request, 'registration/registration_form.html', {'form': form})

    # else:
    return render(request, 'registration/registration_form.html', {'form': form})



