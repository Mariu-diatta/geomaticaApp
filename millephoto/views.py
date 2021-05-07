
from .models import Users,Album,Photo
from .serializers import UsersSerializer,AlbumSerializer,PhotoSerializer
from rest_framework import status, generics

# classe Users
class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersDetail(generics.RetrieveUpdateAPIView):
    queryset = Users
    serializer_class = UsersSerializer
# classe Album
class AlbumsList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetail(generics.RetrieveUpdateAPIView):
    queryset = Album
    serializer_class = AlbumSerializer

# classe Photo
class PhotosList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotosDetail(generics.RetrieveUpdateAPIView):
    queryset = Photo
    serializer_class = PhotoSerializer