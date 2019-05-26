from django.contrib import admin
from django.urls import path, include
import crudapp.views
import diaryapp.views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('crudapp.urls')),
     path('diary/',include('diaryapp.urls')),
]
