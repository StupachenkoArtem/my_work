from django.conf import settings
from django.urls import path, re_path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('', index, name='home'),
    path('collections/', CollectionView.as_view(), name='collections'),
    # path('photo/<int:collection_id>/', photo_view, name='photos'),
    path("MIKHAL'CHUK/", mikhalchuk, name="MIKHAL'CHUK"),
    path('contact/', contact, name='contact'),
    path('newcollection/', NewCollectionView.as_view(), name='new_collection'),
    path('jackets/', JacketsView.as_view(), name='jackets'),
    path('dress/', DressView.as_view(), name='dress'),
    path('shirts_and_blouses/', ShirtsAndBlousesView.as_view(), name='shirts_and_blouses'),
    path('trousers_and_skirts/', TrousersAndSkirtsView.as_view(), name='trousers_and_skirts'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
