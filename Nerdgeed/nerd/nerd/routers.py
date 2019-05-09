from apps.interview_broadcast.api.viewsets  import DashViewSet ,UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()

# Events Section Endpoints Router
router.register('addcompany', viewset=DashViewSet)
router.register('user', viewset=UserViewSet)