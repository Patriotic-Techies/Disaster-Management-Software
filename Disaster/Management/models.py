# models.py

from django.db import models

class Organization(models.Model):
    Organization_name = models.CharField(max_length=100)
    Organization_type = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    
    admin_name = models.CharField(max_length=100, default='')
    team_member_count = models.IntegerField(default=0)

    # New fields for storing latitude and longitude
    Organization_location = models.CharField(max_length=255, blank=True, null=True)  # Field to store location
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)





    
