from django.urls import path
from .views import VisitedHome, AddPost, logout_user


urlpatterns = [
    path('', VisitedHome.as_view(), name='home'),  # http://127.0.0.1:8000/
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('logout/', logout_user, name='logout'),
    # path('login/', login, name='login'),
]
