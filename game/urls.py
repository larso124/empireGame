from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_name, name="index"),
    path("play/", views.game_play, name="game play"),
    path("waitroom/", views.wait_room, name=" wait room"),
    path("reset/", views.reset, name="reset"),
    path("setup/", views.setup, name="setup"),
    path("crossout/<int:id>", views.crossout, name="crossout")

]