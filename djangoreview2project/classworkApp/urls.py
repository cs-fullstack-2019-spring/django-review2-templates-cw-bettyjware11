from django.urls import path

from . import views

urlpatterns = [
    # fixed path
    path('songs/', views.list_songs, name='list_songs'),
#     path that takes parameters...
    path('songs/<int:song_id>', views.list_song, name='song_details'),
    path('songs/<int:song_id>', views.list_song2, name='filtered_details'),

]