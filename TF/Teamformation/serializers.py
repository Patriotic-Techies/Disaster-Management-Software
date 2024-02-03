# serializers.py

from rest_framework import serializers
from .models import UserProfile, Team

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        extra_kwargs = {
            'profession': {'required': True}  # Assuming 'profession' is the new field
        }

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
