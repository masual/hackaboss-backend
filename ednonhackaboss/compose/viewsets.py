from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from compose.models import Compose
from compose.serializers import ComposeSerializer

class ComposeViewSet(viewsets.ModelViewSet):
    queryset = Compose.objects.all()
    serializer_class = ComposeSerializer