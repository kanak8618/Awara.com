from django.urls import path

from . import views

urlpatterns = [
    path('',views.BLOG, name='blog'),
    path('blog/<slug:slug>',views.BLOG_DETAIL, name='blog_detail'),
]
