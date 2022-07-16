from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [
    path('aaa', views.Login.as_view(), name='login'),
]
