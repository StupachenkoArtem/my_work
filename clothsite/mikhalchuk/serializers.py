from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from mikhalchuk.models import *


class CollectionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Collection
        fields = '__all__'
