from rest_framework import serializers
from api import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.user
        fields = "__all__"
