from django.contrib.auth.models import User
from django.db import models


class Places(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Посещенные места'
        verbose_name_plural = 'Посещенные места'
        ordering = ['-time_create']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
