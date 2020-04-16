from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Link


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username','password', 'is_staff']

class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['descricao','url_original','url_encurtado','contador']
