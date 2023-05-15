from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import *
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

def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'visited/addpost.html', {'menu': menu, 'form': form})

def login(request):
    return HttpResponse('Авторизация')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')