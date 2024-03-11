from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUser, RegisterUser
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


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
        form_register = RegisterUser(request.POST)

        if form_register.is_valid():
            user = form_register.save(commit=False)
            user.set_password(form_register.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html')
        
        else:
            return render(request, 'users/register.html', {'form' : form_register})


    form_register = RegisterUser()

    return render(request, 'users/register.html', {'form' : form_register})

