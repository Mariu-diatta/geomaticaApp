from rest_framework import serializers
from .models import Users, Album,Photo


#Serialisation de la classe Users
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=['user_pseudo','user_email','user_tel','user_phone','user_passe','user_comment']

#Serialisation de la classe Album
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model=Album
        fields=['album_pseudo','album_titre','album_type','album_photo','album_label']

#serialisation model photo
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Photo
        fields=['photo','photo_type','photo_label','photo_coord','album_pseudo','user_pseudo']

