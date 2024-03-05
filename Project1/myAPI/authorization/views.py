from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

list = [{'title':'LOGIN', 'url_name':'login'},
        {'title':'REGISTRSTION', 'url_name':'registration'}
    ]


def index(request):

    return render(request, 'index.html', {'list': list})

def login(request):
    return render(request, 'login.html', {'list': list, 'title':'login', 'content':'Я не устал'})


def registration(request, id:str=1):
    
    post = get_object_or_404(Authorization, pk=id)

    context = {
        'post': post,
        'post_login': post.login,
        'cat_id': post.cat_id
    }

    return render(request, 'post.html', context = context)

def archive(request, year):

    if int(year) > 2024:
        return redirect('home', permanent=True) #перемещение(permanent=True задает response 301)
    elif int(year) < 1500:
        raise Http404() #будет вызван pageNotFound()

    return HttpResponse(f"<h1>Регистрация {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')