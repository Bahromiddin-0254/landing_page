from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
app_name='main'

urlpatterns = [
    path('', index,name='index'),
    path('admin/',admin,name='admin'),
    path('login/',login,name='login'),
    path('signup/',signup,name='register'),
]