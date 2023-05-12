from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [{"title": 'Places Remember', 'url_name': 'home'},
        {"title": 'Войти с помощью Google', 'url_name': 'login'},
        ]
def index(request):
    posts = Places.objects.all()
    context = {
        "posts": posts,
        "menu": menu,
    }
    return render(request, 'visited/index.html', context=context)

def newpost(request):
    return HttpResponse('Добавить новое место')

def login(request):
    return HttpResponse('Авторизация')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')