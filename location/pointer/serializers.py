# serializers.py

from rest_framework import serializers
from .models import Organization, TeamMember, UserLocation



class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = ['organization_name', 'address', 'latitude', 'longitude']



class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['name', 'email', 'phone', 'role']

class OrganizationSerializer(serializers.ModelSerializer):
    team_members = TeamMemberSerializer(many=True, required=False)

    class Meta:
        model = Organization
        fields = '__all__'

    def create(self, validated_data):
        team_members_data = validated_data.pop('team_members', [])
        organization = Organization.objects.create(**validated_data)

        for team_member_data in team_members_data:
            TeamMember.objects.create(organization=organization, **team_member_data)

        return organization
