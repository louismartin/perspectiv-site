from django.urls import path

from . import views


urlpatterns = [
    path("", views.app, name="app"),
    path("manage/", views.manage, name="manage"),
]
