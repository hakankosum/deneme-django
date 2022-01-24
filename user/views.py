from enum import auto
from django.shortcuts import render,redirect
from .forms import loginForm, registerForm,loginForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auto_login
from django.contrib.auth import logout as auto_logout
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST" :
        form = registerForm(request.POST)
        if form.is_valid():
                username=form.cleaned_data.get("username")
                password=form.cleaned_data.get("password")
                newUser = User(username = username)
                newUser.set_password(password)
                newUser.save()
                auto_login(request,newUser)
                messages.success(request,"Succesful register")
                return redirect("index")
        else:
            form = registerForm()
            context={
                "form":form
            }
            return render(request,"register.html",context)
                
    else:
        form = registerForm()
        context={
            "form":form
        }
        return render(request,"register.html",context)

def login(request):
    if request.method == "POST" :
        form = loginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user = authenticate(username = username,password=password)
            if user is None:
                messages.info(request,"Error , ,invalid password or username")
                return render(request,"login.html")
            messages.info(request,"Successful login")
            auto_login(request,user)
            return render(request,"index.html")
    else:
        form = loginForm()
        context={
            "form":form
        }
        return render(request,"login.html",context)


        
def logout(request):
    messages.success(request,"Successfuly logout")
    auto_logout(request)
    return redirect("index")