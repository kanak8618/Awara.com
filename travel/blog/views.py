from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
# Create your views here.

def BLOG(request):
    post = Post.objects.all().order_by('id')
    popular = Post.objects.filter(popular=True).order_by('-id')[0:5]
    category = Blog_Ctgry.objects.all()
    insta_feed = InstaFeed.objects.all()

    paginator = Paginator(post, 6)
    page_no = request.GET.get('page')
    post = paginator.get_page(page_no)

    context = {

        'post': post,
        'popular': popular,
        'category': category,
        'insta_feed': insta_feed,
    }
    return render(request,'blog/blog list.html',context)

def BLOG_DETAIL(request,slug):
    post = Post.objects.filter(slug = slug)
    posts = Post.objects.all().order_by('-id')[0:2]
    popular = Post.objects.filter(popular=True).order_by('-id')[0:10]
    category = Blog_Ctgry.objects.all()
    insta_feed = InstaFeed.objects.all().order_by('-id')[0:5]
    context = {

        'post': post,
        'posts': posts,
        'popular': popular,
        'category': category,
        'insta_feed': insta_feed,
    }
    return render(request,'blog/blog detail.html',context)