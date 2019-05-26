from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('diary/', views.diary, name = "diary"),
     path('diary/<int:blog_id>/', views.detail, name='ddetail'),
     path('diary/new/', views.new, name='dnew'),
     path('diary/create/', views.create, name='diary_create'),
]