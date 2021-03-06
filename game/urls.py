"""touchcou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='game-home'),
    path('list', views.GamesListView.as_view(), name='game-list'),
    path('create', views.GameCreateView.as_view(), name='game-create'),
    # re_path('join/(?P<game_id>[0-9]+)', views.GameJoinView.as_view(), name='game-join'),
    re_path('prepare/(?P<game_id>[0-9]+)', views.GamePlayerPrepareView.as_view(), name='game-player-prepare'),
    re_path('board/(?P<game_id>[0-9]+)', views.GameBoardView.as_view(), name='game-board'),
]
