from django.test import TestCase
from mikhalchuk.models import Collection, Photo
from django.contrib.auth.models import User


class CollectionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        Collection.objects.create(name='Test Collection', main_photo='test.jpg', user=test_user1)

    def test_name_label(self):
        collection = Collection.objects.get(id=1)
        field_label = collection._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_user_label(self):
        collection = Collection.objects.get(id=1)
        field_label = collection._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'Пользователь')

    def test_name_max_length(self):
        collection = Collection.objects.get(id=1)
        max_length = collection._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)


class PhotoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_collection = Collection.objects.create(name='Test Collection', main_photo='test.jpg', user=test_user1)
        Photo.objects.create(collection=test_collection, image='test_image.jpg')

    def test_collection_foreign_key(self):
        photo = Photo.objects.get(id=1)
        collection = Collection.objects.get(id=1)
        self.assertEquals(photo.collection, collection)
