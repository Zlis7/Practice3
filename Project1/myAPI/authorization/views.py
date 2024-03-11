from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .forms import *

list = [{'title':'LOGIN', 'url_name':'login'},
        {'title':'REGISTRSTION', 'url_name':'registration'}
    ]


def index(request):

    return render(request, 'index.html', {'list': list})

def login(request):

    post = Authorization.objects.all()

    return render(request, 'registration.html', {'list': list, 'title':'login', 'content':'Я не устал', 'post': post})


def registration(request, id:str=1):

    post = get_object_or_404(Authorization, pk=id)
    #  post = get_object_or_404(Authorization, slugURL=id)

    context = {
        'post': post,
        'post_login': post.login,
        'cat_id': post.cat_id,
        'form': addNewUser()
    }

    if request.method == 'POST':
        form = addNewUser(request.POST, request.FILES)
        if form.is_valid():
            
            try:
                #Authorization.objects.create(**form.cleaned_data) - если форма к БД не привязана
                
                form.save()

                return redirect('home') #если форма к БД не привязана
                
            except:
                form.add_error(None, 'Ошибка добавления поста')
            
        context['form'] = form
    else:
        form = addNewUser()

    return render(request, 'post.html', context = context)

def archive(request, year):

    if int(year) > 2024:
        return redirect('home', permanent=True) #перемещение(permanent=True задает response 301)
    elif int(year) < 1500:
        raise Http404() #будет вызван pageNotFound()

    return HttpResponse(f"<h1>Регистрация {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')