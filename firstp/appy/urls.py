from django.urls import path
from . import views

urlpatterns = [
               path("musicshop/", views.music1, name="music1"),
               path("musicshop/home/", views.home, name = "home"),
               path("musicshop/signup/", views.signup, name = "signup"),
               path("musicshop/home/drums", views.drums, name = "drums"),
               path("musicshop/add-info/", views.signup, name = "add-info"),]