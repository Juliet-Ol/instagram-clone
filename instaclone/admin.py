
from django.contrib import admin
from .models import Image, Comment, Post

# admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Post)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
