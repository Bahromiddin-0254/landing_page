from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignUpForm
from django.shortcuts import reverse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from main.models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')
@login_required(login_url="/login/")
def admin(request):
    
    employees = Employee.objects.all()
    dates = Date.objects.all()
    return render(request, 'admin.html', {'employees':employees, 'dates':dates})


def login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                if user.is_staff:
                    return redirect(reverse('main:admin'))
                else:
                    return redirect(reverse('main:index'))
    
    return render(request, 'login.html',{'form':form})
def signup(request):
    msg = None
    success = False
    form = SignUpForm(request.POST or None)
    if request.method == "POST": 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)

            msg = """User created successfully."""
            success = True
            if success:
                return redirect("/")
            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    return render(request, "signup.html", {"form": form, "msg": msg, "success": success})
            