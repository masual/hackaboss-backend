from rest_framework import serializers
from compose.models import Compose

class ComposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compose
        fields = '__all__'