from django.contrib import admin
from django.urls import path

from . import views

app_name = 'song'

urlpatterns = [
    path('<int:pk>/', views.index, name='index'),
]