# from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse('This is an instagram clone')



