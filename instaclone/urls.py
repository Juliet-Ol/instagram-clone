from django.urls import path
from . import views
from instaclone import views

urlpatterns=[
    # path('',views.welcome,name = 'welcome'),
    path('', views.index, name='index')
]