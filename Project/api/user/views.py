from django.shortcuts import render
from django.http import JsonResponse

NAME_INPUT_LOGIN = 'login'
NAME_INPUT_PASSWORD = 'password'

def home(request):
    return HttpResponse('home')

def login(request):

    if request.method == 'GET':
       # print(f"LOGIN: {request.GET[NAME_INPUT_LOGIN]}\nPASSWORD: {request.GET[NAME_INPUT_PASSWORD]}")

        return JsonResponse({'name':'Denis'})

def logout(request):
    return HttpResponse('logout')

def register(request):
    return HttpResponse('register')

