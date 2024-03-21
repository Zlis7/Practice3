from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def home(request):
    return HttpResponse('home')

def login(request):
    return JsonResponse({'Access': True})

def logout(request):
    return HttpResponse('logout')

def register(request):
    return HttpResponse('register')

