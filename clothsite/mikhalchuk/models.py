from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=255)
    main_photo = models.ImageField(upload_to='collection_photos')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Photo(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='collection_photos')

    def __str__(self):
        return f"{self.collection.name} - Photo {self.pk}"


class Dress(models.Model):
    name = models.CharField(max_length=255)
    main_photo = models.ImageField(upload_to='Dress_photos')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DressPhoto(models.Model):
    Dress = models.ForeignKey(Dress, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Dress_photos')

    def __str__(self):
        return f"{self.Dress.name} - Photo {self.pk}"


class Jackets(models.Model):
    name = models.CharField(max_length=255)
    main_photo = models.ImageField(upload_to='Jackets_photos')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class JacketsPhoto(models.Model):
    Jackets = models.ForeignKey(Jackets, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Jackets_photos')

    def __str__(self):
        return f"{self.Jackets.name} - Photo {self.pk}"


class NewCollection(models.Model):
    name = models.CharField(max_length=255)
    main_photo = models.ImageField(upload_to='NewCollection_photos')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class NewCollectionPhoto(models.Model):
    NewCollection = models.ForeignKey(NewCollection, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='NewCollection_photos')

    def __str__(self):
        return f"{self.NewCollection.name} - Photo {self.pk}"


class ShirtsAndBlouses(models.Model):
    name = models.CharField(max_length=255)
    main_photo = models.ImageField(upload_to='ShirtsAndBlouses_photos')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ShirtsAndBlousesPhoto(models.Model):
    ShirtsAndBlouses = models.ForeignKey(ShirtsAndBlouses, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ShirtsAndBlouses_photos')

    def __str__(self):
        return f"{self.ShirtsAndBlouses.name} - Photo {self.pk}"


class TrousersAndSkirts(models.Model):
    name = models.CharField(max_length=255)
    main_photo = models.ImageField(upload_to='TrousersAndSkirts_photos')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TrousersAndSkirtsPhoto(models.Model):
    TrousersAndSkirts = models.ForeignKey(TrousersAndSkirts, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='TrousersAndSkirts_photos')

    def __str__(self):
        return f"{self.TrousersAndSkirts.name} - Photo {self.pk}"
