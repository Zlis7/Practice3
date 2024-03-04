from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

list = ['О сайте', 'Товары', 'Отзывы', 'События']


def index(request):
    return render(request, 'index.html', {'list': list, 'title':'index', 'content':'Я устал'} )

def login(request):
    return render(request, 'login.html', {'list': list, 'title':'login', 'contant':'Я не устал'})

def registration(request, id:str=0) -> HttpResponse:
    posts = Authorization.objects.all()
    return render(request, 'registration.html', {'post': posts, 'list': list, 'title':'registration', 'contant':'Я чуть устал', 'id':id})

def archive(request, year):

    if int(year) > 2024:
        return redirect('home', permanent=True) #перемещение(permanent=True задает response 301)
    elif int(year) < 1500:
        raise Http404() #будет вызван pageNotFound()

    return HttpResponse(f"<h1>Регистрация {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')