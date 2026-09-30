from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MeditationSession, ActivityLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']

class MeditationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationSession
        fields = '__all__'
    
    def validate_duration_minutes(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be positive.")
        return value

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'
