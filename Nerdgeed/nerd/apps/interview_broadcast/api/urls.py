from django.urls import path, re_path, include
# from apps.interview_broadcast.api.views import JobList
from apps.interview_broadcast.api.viewset import DashViewSet,UserViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'dash', DashViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('', include(router.urls)),
]