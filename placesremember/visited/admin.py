from django.contrib import admin

from .models import *

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment', 'time_create', 'user_id')
    list_display_links = ('name', )
    search_fields = ('name', )
    list_filter = ('user_id', )

admin.site.register(Places, PlacesAdmin)

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'avatar', 'user_id')

admin.site.register(Profile)