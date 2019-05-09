from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.interview_broadcast.models import (
    Dashbooard, popupuser
    
)
from .serializers import (
    dashSerializer, userSerializer

)
                                  

class DashViewSet(viewsets.ModelViewSet):
    queryset = Dashbooard.objects.all()
    serializer_class = dashSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    queryset = popupuser.objects.all()
    serializer_class = userSerializer

