from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    disaster_type = models.CharField(max_length=100)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    


class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    disaster_type = models.CharField(max_length=100)
