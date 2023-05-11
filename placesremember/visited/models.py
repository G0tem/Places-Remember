from django.contrib.auth.models import User
from django.db import models

class Places(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
