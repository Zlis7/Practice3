from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import *


def index(request):
    return HttpResponse('index')

def login_user(request):

    if request.method == 'POST':
        form = LoginUser(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data
            user = authenticate(request, username = form_data['username'],
                            password = form_data['password'])
            
            if user and user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse('users:home'))
    
    form_login = LoginUser()

    return render(request, 'users/login.html', {'form':form_login})



def register_user(request):

    if request.method == 'POST':
        form_register = RegisterUser(request.POST, request.FILES)

        if form_register.is_valid():
            user = form_register.save(commit=False)
            user.set_password(form_register.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html')
        
        else:
            return render(request, 'users/register.html', {'form' : form_register})


    form_register = RegisterUser()

    return render(request, 'users/register.html', {'form' : form_register})


def all_users(request):

    users = User.objects.all()

    return render(request, 'users/allusers.html', {'dataUser': users})



def handle_uploaded_file(f):
    with open(f"uploads/users/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def media_download(request):

    if request.method == 'POST':
        
        form = UploadImageForm(request.POST, request.FILES)

        if form.is_valid():
            #handle_uploaded_file(form.cleaned_data['photo'])
            fp = UploadFiles(photo = form.cleaned_data['photo'])
            fp.save()

        return render(request, 'users/mediadownload.html', {'form':form})

    else:

        form = UploadImageForm()

        return render(request, 'users/mediadownload.html', {'form':form})

