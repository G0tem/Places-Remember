from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import *
from .models import *
from .utils import *

class VisitedHome(DataMixin, ListView):
    paginate_by = 3
    model = Places
    template_name = 'visited/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        user_id = self.request.user.id
        return Places.objects.filter(user=user_id)  # нужно чтобы фильтровало только id авторизованного
        # return self.request.user.places_set.all()
        # user = self.request.user
        # return user.places_set.all() if user else None

class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'visited/addpost.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить воспоминания')
        context['form'].initial['user'] = self.request.user
        return dict(list(context.items()) + list(c_def.items()))

def login(request):
    return HttpResponse('Авторизация')

def logout_user(request):
    logout(request)
    return redirect('home')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

