from rest_framework import routers
from compose.viewsets import ComposeViewSet

router = routers.DefaultRouter()
router.register(r'compose', ComposeViewSet)