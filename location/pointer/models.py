from django.db import models
from django.contrib.auth.models import User

class UserLocation(models.Model):
    
    organization_name = models.CharField(max_length=255,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.organization_name} - {self.latitude}, {self.longitude}"





class TeamMember(models.Model):
    ROLES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('helper', 'Helper'),
        ('fighter', 'Fighter'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return self.name

class RescueOperation(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):
        return f"Rescue Operation for {self.organization.organization_name}"

class Organization(models.Model):
    ORG_TYPES = [
        ('flood', 'Disaster - Flooding'),
        ('earthquake', 'Disaster - Earthquake'),
        ('tsunami', 'Disaster - Tsunami'),
        ('cyclone', 'Disaster - Cyclone'),
        ('wildfire', 'Disaster - Wildfire'),
        ('other', 'Other'),
    ]

    organization_name = models.CharField(max_length=255)
    organization_type = models.CharField(max_length=20, choices=ORG_TYPES)
    address = models.TextField(blank=True,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    team_members_count = models.IntegerField()
    
    def __str__(self):
        return self.organization_name
