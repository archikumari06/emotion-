# from django.contrib import admin
from django.urls import path , include

from . import views
 

urlpatterns = [
    path('', views.index, name='index'),
    path('feature/', views.feature, name='feature'),
    path('about/', views.about, name='about'),
    path('happy/', views.happy, name='happy'),
    path('sad/', views.sad, name='sad'),
    path('neutral/', views.neutral, name='neutral'),
    path('fear/', views.fear, name='fear'),
    path('disgust/', views.disgust, name='disgust'),
    path('surprise/', views.surprise, name='surprise'),
    path('angry/', views.angry, name='angry'),
    path('check/', views.check, name='check'),
]