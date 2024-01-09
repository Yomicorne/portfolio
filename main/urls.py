from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("social_media/", views.social_media, name="social_media"),
    path("projects/", views.projects, name="projects"),
    path("game/", views.game, name="game"), 
]