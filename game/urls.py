from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("play/", views.game_play, name="game play")
]