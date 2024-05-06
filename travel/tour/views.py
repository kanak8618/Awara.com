from django.shortcuts import render,redirect
from .models import *
from django.db.models import Max, Min, Sum
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.

def INDEX(request):
    slider = Hero_Slider.objects.all().order_by('-id')
    hero_featurs = Hero_Featurs.objects.all().order_by('-id')[0:3]
    category = Tour_Ctgry.objects.all().order_by('-id')[0:4]
    services = Service.objects.all().order_by('-id')

    context ={
        'services':services,
        'slider':slider,
        'category':category,
        'packages':Package.get_all_package(),
        'hero_featurs':hero_featurs,
    }
    return render(request, 'main/index.html',context)

def PACKAGE(request):
    package = Package.get_all_package().order_by('-id')
    category = Tour_Ctgry.objects.all().order_by('id')
    slider = Package_Slider.objects.all().order_by('id')
    min_price = Package.objects.all().aggregate(Min('price'))
    max_price = Package.objects.all().aggregate(Max('price'))

    catID = request.GET.get('category')
    Filt_price = request.GET.get('FilterPrice')

    if catID:
        package = Package.get_package_by_category_id(catID)
    elif Filt_price:
        package = Package.get_package_by_price(Filt_price)
    else:
        package = Package.get_all_package()

    paginator = Paginator(package, 12)
    page_no = request.GET.get('page')
    package = paginator.get_page(page_no)

    context = {
        'package': package,
        'category': category,
        'slider': slider,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'main/package.html', context)


def PACKAGE_DETAIL(request, slug):
    category = Tour_Ctgry.objects.all().order_by('id')[0:5]
    package = Package.objects.get(slug=slug)

    context = {
        'category': category,
        'package': package,
    }
    return render(request, 'main/package detail.html', context)

def CHECKOUT(request, slug):
    return render(request, 'checkout/checkout.html')

def PAGE_NOT_FOUND(request):
    category = Tour_Ctgry.get_all_category(Tour_Ctgry)
    context = {
        'category': category
    }
    return render(request, 'error/404.html',context)

def SERVICE(request):
    services = Service.objects.all().order_by('-id')
    context = {
        'services': services,
    }
    return render(request, 'main/service.html', context)

def CONTACT(request):
    context = {
    }
    return render(request, 'main/contact.html', context)

def ABOUT(request):
    context = {

    }
    return render(request, 'main/about.html', context)