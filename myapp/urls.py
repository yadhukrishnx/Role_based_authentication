
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("register/", views.userRegistration, name="register"),
    path("home/", views.home, name="home"),
    path("adminhome/", views.adminhome, name="adminhome"),
]
