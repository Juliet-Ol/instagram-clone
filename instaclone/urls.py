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
    path('profile', views.profile, name='profile'),
    path('edit-profile', views.editProfile, name='edit-profile'),
    path('post', views.post, name='new-post'),
    path('comment', views.comment, name='add-comment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)