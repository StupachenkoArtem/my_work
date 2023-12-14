from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from clothsite import settings
from mikhalchuk.views import *
from rest_framework import routers
from mikhalchuk.viewsets import CollectionAPIDestroy, CollectionAPIUpdate, CollectionAPIList

# router = routers.DefaultRouter()
# router.register(r'collection', CollectionViewSet)
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mikhalchuk.urls')),
    path('api/v1/collection/', CollectionAPIList.as_view()),
    path('api/v1/collection/<int:pk>/', CollectionAPIUpdate.as_view()),
    path('api/v1/collectiondelete/<int:pk>/', CollectionAPIDestroy.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/v1/', include(router.urls)),
    # path('api/v1/collectionlist/', CollectionViewSet.as_view({'get': 'list'})),
    # path('api/v1/collectionlist/<int:pk>/', CollectionViewSet.as_view({'put': 'update'})),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
