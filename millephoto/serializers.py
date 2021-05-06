from rest_framework import serializers
from .models import Users, Album,Photo

#Serialisation de la classe Users
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=['pseudo_user','password_user','email_user','tel_user']

#Serialisation de la classe Album
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model=Album
        fields=['pseudo_user','album_pseudo','album_titre','album_label','album_picture','album_type']

#serialisation model photo
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Photo
        fields=['photo_taille','album_pseudo','photo_type','photo_comment','photo_coord']

