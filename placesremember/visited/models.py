from django.contrib.auth.models import User
from django.db import models

class Places(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    сoord = models.CharField(max_length=255)
    location_name = models.CharField(max_length=255)
    location_comment = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
