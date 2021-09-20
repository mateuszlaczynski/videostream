from django.contrib import admin
from django.urls import path
from .views import (home, detail, add_video,
                    like, dislike, subbox,
                    delete_comment, edit_comment,
                    search, dashboard, edit_video,
                    delete_video)

urlpatterns = [
    path('', home, name="home"),
    path('watch/<slug:video_slug>/', detail, name="detail"),
    path('add-video/', add_video, name="add-video"),
    path('like/<int:id>/', like, name="like-video"),
    path('dislike/<int:id>/', dislike, name="dislike-video"),  
    path('subbox/', subbox, name="subbox"),
    path('comment/<int:id>/delete', delete_comment, name="delete-comment"),
    path('comment/<int:id>/edit', edit_comment, name="edit-comment"),
    path('search/', search, name="search"),
    path('dashboard/', dashboard, name="dashboard"),
    path('edit/<slug:video_slug>/', edit_video, name='edit-video'),
    path('delete/<slug:video_slug>/', delete_video, name='delete-video'),
]