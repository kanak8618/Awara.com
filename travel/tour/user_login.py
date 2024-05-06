from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .EmailBackEnd import EmailBackEnd
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check email
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email are Already Exists !')       #show the warning messsage if user already register
            return redirect('register')

        # check username
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username are Already exists !')    #show the warning messsage if email already register
            return redirect('register')

        user = User(         #if user is not register then set data in table
            username=username,
            email=email,
        )
        user.set_password(password)    #set password
        user.save()     #save user info
        return redirect('login')

    return render(request, 'registration/register.html')

def DO_LOGIN(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = EmailBackEnd.authenticate(request, username=email, password=password)
        if user != None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('login')

def Logout_Request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")

@login_required(login_url='login')
def PROFILE(request):
    return render(request, 'registration/profile.html')

@login_required(login_url='login')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_id = request.user.id

        user = User.objects.get(id=user_id)         #if here id is ge then update old data with new data otherwise add new data

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":   # if user want to update password, it will be set new password other wise directly save other new info..
            user.set_password(password)

        user.save()
        messages.success(request, 'Profile Are Successfully Updated. ')
        return redirect('profile')

