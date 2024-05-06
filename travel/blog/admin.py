from django.contrib import admin
from .models import *
# Register your models here.

class Blog_Ctgry_Admin(admin.ModelAdmin):
    model = Blog_Ctgry
    list_display = ["title","date","image"]

class InstaFeed_Admin(admin.ModelAdmin):
    model = InstaFeed
    list_display = ["title"]

class Post_Admin(admin.ModelAdmin):
    model = Post
    list_display = ["blog_title","Tags","popular","Category","instafeed"]
    list_editable = ["popular","Category"]

admin.site.register(Blog_Ctgry,Blog_Ctgry_Admin)
admin.site.register(InstaFeed,InstaFeed_Admin)
admin.site.register(Post,Post_Admin)