from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import MeditationSession, ActivityLog
from .serializers import UserSerializer, MeditationSessionSerializer, ActivityLogSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MeditationSessionViewSet(viewsets.ModelViewSet):
    queryset = MeditationSession.objects.all()
    serializer_class = MeditationSessionSerializer

class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
