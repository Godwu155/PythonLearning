"""Accounts URL Configuration"""

from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    #包含默认的身份验证URL
    path('', include('django.contrib.auth.urls')),
    #注册界面
    path('register/', views.register, name='register')
]