from django.contrib import admin
from django.urls import path
from .views import listtweet,addtweet,addtweetbyform
urlpatterns = [
    path('',listtweet,name='listtweet'),
    path('addtweet/',addtweet,name='addtweet'),
    path('addtweetbyform/',addtweetbyform,name='addtweetbyform')
]
