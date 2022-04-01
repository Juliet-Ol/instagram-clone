from django.shortcuts import render
from django.http import HttpResponse
from .models import Image


# def welcome(request):
#     return HttpResponse('This is an instagram clone')

def index(request): 
    image = Image.objects.all() 
    ctx = {'image':image}
    
    return render(request,'instaclone/index.html', ctx)



