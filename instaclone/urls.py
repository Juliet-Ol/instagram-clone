from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from instaclone import views

urlpatterns=[
    # path('',views.welcome,name = 'welcome'),
    path('', views.index, name='index'),
    path('load/', views.loadImage, name='load'),
    path('accounts/register/', views.register, name='register'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)