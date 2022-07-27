from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.models import *
from django.db import IntegrityError

# Create your views here.

def customer_login_view(request):
    
    if request.method == "POST":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username = username , password = password)
        print(user)
        if user == None:
            # return HttpResponse("masa go and sleep")
            return HttpResponse("try again")
        elif username =="admin":
            # login(request, user)
            return redirect("dashboard:admin_dashboard")
        else:
            login(request, user)
            return redirect("main:user_page")
    return render(request,'login/customer_login.html')

    

def service_provider_login_view(request):
    if request.method == "POST":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username = username , password = password)
        print(user)
        if user == None:
            # return HttpResponse("masa go and sleep")
            return HttpResponse("try again")
        elif username =="admin":
            # login(request, user)
            return redirect("dashboard:admin_dashboard")
        else:
            login(request, user)
            return redirect("main:service_provider_page")
   

    return render(request, "login/service_provider_login.html")


def customer_registration_view(request):

    forms = UserSignUp()
    if request.method == 'POST':

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(request.POST)

        data_username = User.objects.filter(username = username).first
        try:
            user = User.objects.create(
                username = username,
                email = email,
            )
            user.set_password(password)
            user.save()
        except IntegrityError as e: 
                return HttpResponse("sdfasdfaskdhsajdfhksdf")

        # return redirect("auth:user_login")
        return HttpResponse("Ok its working")

    else:
        pass

    context ={
        'forms':forms
    }
    
    return render(request, "register/customer_register.html",context)

def service_provider_registration_view(request):
    forms = UserSignUp()
    if request.method == 'POST':
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(request.POST)

        data_username = User.objects.filter(username = username).first
        try:
            user = User.objects.create(
                username = username,
                email = email,
            )
            user.set_password(password)
            user.save()
        except IntegrityError as e: 
                return HttpResponse("sdfasdfaskdhsajdfhksdf")

        # return redirect("auth:user_login")
        return HttpResponse("Ok its working")

    else:
        pass

    context ={
        'forms':forms
    }
    
    return render(request, "register/service_provider_register.html",context)



def login_register_view(request):

    return render(request, "login/login.html")