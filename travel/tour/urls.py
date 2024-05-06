from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views, user_login

urlpatterns = [
    path('',views.INDEX, name='index'),
    path('service/',views.SERVICE, name='service'),
    path('contact-us/',views.CONTACT, name='contact-us'),
    path('about-us/',views.ABOUT, name='about-us'),
    path('404/',views.PAGE_NOT_FOUND, name='404'),

    path('package/',views.PACKAGE, name='package'),
    path('package/<slug:slug>', views.PACKAGE_DETAIL, name='package_detail'),

    path('accounts/register', user_login.REGISTER, name='register'), #register.html path
    path('accounts/', include('django.contrib.auth.urls')),       #login.html path   -login is builtin django module not necessary to build view of that -'accounts/login
    path('doLogin/', user_login.DO_LOGIN, name='doLogin'),
    path("logout", user_login.Logout_Request, name="logout"),
    path('accounts/profile/', user_login.PROFILE, name='profile'),     #profile update
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),

    path('checkout/<slug:slug>',views.CHECKOUT, name='checkout'),

    path('blog/',include('blog.urls')),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


