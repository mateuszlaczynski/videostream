from django.contrib import admin
from django.urls import path
from .views import home, detail, add_video

urlpatterns = [
    path('', home, name="home"),
    path('watch/<slug:video_slug>/', detail, name="detail"),
    path('add-video/', add_video, name="add-video"),
]