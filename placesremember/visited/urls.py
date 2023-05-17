from django.urls import path, include

from .views import *

urlpatterns = [
    path('', VisitedHome.as_view(), name='home'),  #http://127.0.0.1:8000/
    path('login/', login, name='login'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('logout/', logout_user, name='logout'),

]
