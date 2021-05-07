from django.core.files.storage import FileSystemStorage
from django.db import models

#la classe Users
class Users(models.Model):
    user_pseudo= models.CharField(max_length=100,unique=True)
    user_email = models.EmailField(max_length=100,unique=True)
    user_tel = models.IntegerField(unique=True)
    user_phone= models.ImageField(null=True,blank=True,upload_to='statics/imageprofiles' )
    user_passe = models.CharField(max_length=100)
    user_comment = models.TextField(max_length=100,blank=False)
    user_is_active=models.BooleanField(default=True)
    user_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_pseudo

#..............................................................................................

class Album(models.Model):
    ALBUM_CHOIX = [
        (1, 'VACCANCE'),
        (2, 'VOYAGE'),
        (3, 'BALADE'),
        (4, 'NATURE'),
        (5, 'FUN'),
    ]
    album_pseudo = models.CharField(max_length=100,unique=True)
    album_titre = models.CharField(max_length=100,blank=False,name=False)
    album_type = models.CharField(max_length=100, choices=ALBUM_CHOIX,default='Nature')
    album_photo = models.ImageField(upload_to='statics/imagealbums',blank=True,null=True)
    album_label = models.TextField(max_length=200, blank=False,null=False)
    album_available = models.BooleanField(default=True)
    album_date = models.DateTimeField(auto_now_add=True)

    # Metadonnee
    class Meta:
        ordering = ['album_pseudo']

    def __str__(self):
        return self.album_pseudo

#..........................................................

class Photo(models.Model):
    PHOTO_CHOIX = [
        (1, 'VACCANCE'),
        (2, 'VOYAGE'),
        (3, 'BALADE'),
        (6, 'NATURE'),
        (7, 'FUN'),
    ]
    photo= models.ImageField(blank=False,null=False,upload_to='statics/images')
    photo_type = models.CharField(max_length=100, choices=PHOTO_CHOIX ,default='Nature')
    photo_label = models.CharField(max_length=200, blank=False)
    photo_coord = models.IntegerField(blank=True, null=True)
    album_pseudo=models.ForeignKey(Album, on_delete=models.CASCADE)
    user_pseudo = models.ForeignKey(Users, on_delete=models.CASCADE)
    photo_date = models.DateTimeField(auto_now_add=True)

    # Metadonnee
    class Meta:
        ordering = ['photo_label']

    def __str__(self):
        return "%s %s %s %s" % (self.user_pseudo,self.album_pseudo, self.photo_type, self.photo_date)