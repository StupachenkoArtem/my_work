from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from mikhalchuk.models import Collection
from mikhalchuk.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from mikhalchuk.serializers import CollectionSerializer


class CollectionAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class CollectionAPIList(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = CollectionAPIListPagination


class CollectionAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CollectionAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAdminOrReadOnly, )
