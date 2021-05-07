from django.db import models

class Users(models.Model):
    pseudo_user = models.CharField(max_length=100,primary_key=True)
    passwordUser = models.CharField(max_length=100,default=True)
    email_user = models.EmailField(max_length=254)
    tel_user = models.IntegerField()
    date_user = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pseudo_user


class Album(models.Model):
    ALBUM_CHOIX = [
        (1, 'VACCANCE'),
        (2, 'VOYAGE'),
        (3, 'BALADE'),
        (4, 'NATURE'),
        (5, 'FUN'),
    ]
    pseudo_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    album_pseudo = models.TextField(max_length=100, primary_key=True)
    album_titre = models.CharField(max_length=200)
    album_label = models.TextField(max_length=100, blank=False)
    album_picture = models.URLField()
    album_type = models.CharField(max_length=200, choices=ALBUM_CHOIX)
    available = models.BooleanField(default=True)
    album_date = models.DateTimeField(auto_now_add=True)

    # Metadonnee
    #class Meta:
       # ordering = ['album_pseudo', '-album_date']

    def __str__(self):
        return "%s %s %s" % (self.album_titre, self.album_label, self.album_date)


class Photo(models.Model):
    PHOTO_CHOIX = [
        (1, 'VACCANCE'),
        (2, 'VOYAGE'),
        (3, 'BALADE'),
        (6, 'NATURE'),
        (7, 'FUN'),
    ]
    photo_taille = models.ImageField(upload_to="images/", blank=False, null=False)
    album_pseudo = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo_type = models.CharField(max_length=100, choices=PHOTO_CHOIX)
    photo_comment = models.TextField(max_length=200, blank=False)
    photo_coord = models.IntegerField(blank=False)
    photo_date = models.DateTimeField(auto_now_add=True)

    # Metadonnee
    #class Meta:
        #ordering = ['album_pseudo', '-photo_date']

    def __str__(self):
        return "%s %s %s %s" % (self.album_pseudo, self.photo_type, self.photo_comment, self.photo_date)