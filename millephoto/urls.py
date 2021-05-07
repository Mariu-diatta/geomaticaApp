from django.urls import path

from .views import PhotosList, AlbumsList, UsersList, PhotosDetail, AlbumDetail, UsersDetail

urlpatterns = [
    path('photos', PhotosList.as_view()),
    path('photos/<int:pk>', PhotosDetail.as_view()),
    path('albums', AlbumsList.as_view()),
    path('albums/<int:pk>', AlbumDetail.as_view()),
    path('users', UsersList.as_view()),
    path('users/<int:pk>', UsersDetail.as_view()),
]