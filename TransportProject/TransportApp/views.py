from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login

# Create your views here.


def registration(request):
    print("Function")
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        cnfpassword = request.POST["cnfpassword"]
        if password == cnfpassword:
            if not Login.objects.filter(username=email).exists():
                logQry = Login.objects.create_user(
                    username=email,
                    password=password,
                    is_active=1,
                    userType="USER",
                    viewPass=password,
                )
                logQry.save()
                regQry = Registration.objects.create(
                    name=name, email=email, phone=phone, loginid=logQry
                )
                regQry.save()
                messages.success(request, "Registered Successfully!")
            else:
                messages.error(request, "Email already exists.")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, "registration.html")


def userLogin(request):
    if request.POST:
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "Login Success")
            return redirect("/index")
    return render(request, "login.html")


def index(request):
    return render(request, "index.html")

def logoutFun(request):
    logout(request)
    return redirect("/")
