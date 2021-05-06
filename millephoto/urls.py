from django.urls import path

from .views import PhotoList, AlbumList, UsersList

urlpatterns = [
    path('photos', PhotoList),
    path('albums', AlbumList),
    path('users', UsersList),
]