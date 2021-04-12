from django.contrib import admin
from django.urls import path
from . import views

app_name = 'modelformsapp'

urlpatterns = [
    path('', views.home, name='dflt'),
    path('signup', views.index, name='modelforms'),
    path('home', views.home, name='home'),
]