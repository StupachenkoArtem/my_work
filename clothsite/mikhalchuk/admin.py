from django.contrib import admin
from .models import *
from django.contrib import admin


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_photo', 'user')
    list_filter = ('user',)
    search_fields = ['name']


admin.site.register(Collection, CollectionAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('collection', 'image')
    list_filter = ('collection',)


admin.site.register(Photo, PhotoAdmin)


class DressAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_photo', 'user')
    list_filter = ('user',)
    search_fields = ['name']


admin.site.register(Dress, DressAdmin)


class DressPhotoAdmin(admin.ModelAdmin):
    list_display = ('Dress', 'image')
    list_filter = ('Dress',)


admin.site.register(DressPhoto, DressPhotoAdmin)


class JacketsAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_photo', 'user')
    list_filter = ('user',)
    search_fields = ['name']


admin.site.register(Jackets, JacketsAdmin)


class JacketsPhotoAdmin(admin.ModelAdmin):
    list_display = ('Jackets', 'image')
    list_filter = ('Jackets',)


admin.site.register(JacketsPhoto, JacketsPhotoAdmin)


class NewCollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_photo', 'user')
    list_filter = ('user',)
    search_fields = ['name']


admin.site.register(NewCollection, NewCollectionAdmin)


class NewCollectionPhotoAdmin(admin.ModelAdmin):
    list_display = ('NewCollection', 'image')
    list_filter = ('NewCollection',)


admin.site.register(NewCollectionPhoto, NewCollectionPhotoAdmin)


class ShirtsAndBlousesAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_photo', 'user')
    list_filter = ('user',)
    search_fields = ['name']


admin.site.register(ShirtsAndBlouses, ShirtsAndBlousesAdmin)


class ShirtsAndBlousesPhotoAdmin(admin.ModelAdmin):
    list_display = ('ShirtsAndBlouses', 'image')
    list_filter = ('ShirtsAndBlouses',)


admin.site.register(ShirtsAndBlousesPhoto, ShirtsAndBlousesPhotoAdmin)


class TrousersAndSkirtsAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_photo', 'user')
    list_filter = ('user',)
    search_fields = ['name']


admin.site.register(TrousersAndSkirts, TrousersAndSkirtsAdmin)


class TrousersAndSkirtsPhotoAdmin(admin.ModelAdmin):
    list_display = ('TrousersAndSkirts', 'image')
    list_filter = ('TrousersAndSkirts',)


admin.site.register(TrousersAndSkirtsPhoto, TrousersAndSkirtsPhotoAdmin)
