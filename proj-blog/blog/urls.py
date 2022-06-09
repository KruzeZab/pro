from django.contrib import admin
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('article/<str:category>/<slug:slug>/', views.BlogView.as_view(), name='article'),
    
]