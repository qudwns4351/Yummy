"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import home.views
import board.views
import chat.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.views.home, name='home'),
    path('auth/', include("member.urls")),

    path('board/list',board.views.list, name='list'),
    path('board/detail',board.views.detail, name='detail'),

    path('chat/chatt',chat.views.chatt, name='chatt'),
    path('chat/chatt/<str:room_name>/', chat.views.room, name='room'),
]
