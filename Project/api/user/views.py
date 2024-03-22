from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .models import UploadFileForm
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, get_token
from django.contrib.auth.decorators import login_required
import json

def status404(request, exception):
    return JsonResponse({
        'message': 'Not found'
    }, content_type='application/json', status = 404, safe=False)


def home(request):
    return HttpResponse('home')

@csrf_exempt
def login(request):
    if request.method == 'POST':

        username = json.loads(request.body).get('email')
        password = json.loads(request.body).get('password')

        user = authenticate(request, username = username, password = password)

        if user and user.is_active:
            auth_login(request, user)

            return JsonResponse({
                'success': True,
                'message': 'Success',
                'token': get_token(request)
            }, content_type='application/json', status = 200, safe=False)
        
        else:
            return JsonResponse({
                "success": False,
                "message": "Login failed",
            }, content_type='application/json', status = 401, safe=False)

    return JsonResponse({'Access': 'GET'})

def logout(request):
    auth_logout(request)

    return JsonResponse({
                "success": True,
                "message": "Logout",
            }, content_type='application/json', status = 200, safe=False)

@csrf_exempt
def register(request):
    if request.method == 'POST':

        username = json.loads(request.body).get('email')
        password = json.loads(request.body).get('password')
        first_name = json.loads(request.body).get('first_name')
        last_name = json.loads(request.body).get('last_name')

        try:
            user = User.objects.create_user(username = username, first_name = first_name,
                last_name = last_name, email = username)
            user.set_password(password)
            user.save()

        except:
            return JsonResponse({
                'success': False,
                'message': "error",
            }, content_type='application/json', status = 422, safe=False)
        
        return JsonResponse({
                'success': True,
                'message': 'Success',
                'token': get_token(request)
            }, content_type='application/json', status = 200, safe=False)


@csrf_exempt    
def fileupload(request):

    if request.method == 'POST':

        try:
            file = UploadFileForm(file = request.FILES['file'])
            file.save()

            return JsonResponse({
                "success": True,
                "message": "Success",
                "name": request.FILES['file'].name,
                "url": 0,
                "file_id": 0
            }, content_type='application/json', status = 200, safe=False)

        except:
            return JsonResponse({
                "success": False,
                "message": "File not loaded",
            }, content_type='application/json', status = 422, safe=False)


        

    

    

        

        






