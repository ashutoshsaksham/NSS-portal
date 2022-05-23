from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="login"),
    path("ngos/", views.ngos, name="ngos"),
    path("ngo/<str:ngo_id>", views.activity, name="activty"),
    path("about/", views.about, name="aboutus"),
    path("contact/", views.contact, name="contactus"),
    path("ngologin/", views.ngologin, name="ngologin"),
]