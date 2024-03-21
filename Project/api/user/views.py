from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return HttpResponse('home')

@csrf_exempt
def login(request):

    if request.method == 'POST':
        print('Hello world')

        return JsonResponse({'Access': 'POST'})

    return JsonResponse({'Access': 'GET'})

def logout(request):
    return HttpResponse('logout')

def register(request):
    return HttpResponse('register')

