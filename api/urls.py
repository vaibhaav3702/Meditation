from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MeditationSessionViewSet, ActivityLogViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sessions', MeditationSessionViewSet)
router.register(r'activity-logs', ActivityLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
