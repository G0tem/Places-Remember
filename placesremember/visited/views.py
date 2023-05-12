from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = ['Places Remember', 'Войти']
def index(request):
    posts = Places.objects.all()
    return render(request, 'visited/index.html', {"posts": posts, "menu": menu})

def newpost(request):
    return HttpResponse('Добавить новое место')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')