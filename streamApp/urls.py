from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('trending/', views.trending, name="trending"),
    path('passbook/', views.passbook, name="passbook"),
]
