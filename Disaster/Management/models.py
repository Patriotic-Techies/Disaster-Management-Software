from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator

class Organization(models.Model):
    ORGANIZATION_TYPES = [
        ('tsunami', 'Tsunami'),
        ('flood', 'Flood'),
        ('cyclone', 'Cyclone'),
        ('Earth Quake', 'Earth Quake'),
        ('storm', 'Storm')
        # Add more choices as needed
    ]

    def validate_phone_number(value):
        if len(value) != 10:
            raise ValidationError("Phone number must be exactly 10 digits.")

    Organization_name = models.CharField(max_length=100)
    Organization_type = models.CharField(max_length=50, choices=ORGANIZATION_TYPES)
    address = models.TextField()
    phone_number = models.CharField(max_length=10, validators=[validate_phone_number])
    admin_name = models.CharField(max_length=100, default='')
    team_member_count = models.IntegerField(default=10, validators=[MinValueValidator(10)])
    Organization_location = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)

    def full_clean(self, *args, **kwargs):
        super().full_clean(*args, **kwargs)

        errors = {}

        if not self.Organization_name:
            errors['Organization_name'] = ['Organization name is required.']

        if not self.Organization_type:
            errors['Organization_type'] = ['Organization type is required.']

        if not self.address:
            errors['address'] = ['Address is required.']

        if not self.phone_number:
            errors['phone_number'] = ['Phone number is required.']

        if not self.admin_name:
            errors['admin_name'] = ['Admin name is required.']

        if self.team_member_count is None:
            errors['team_member_count'] = ['Team member count is required.']

        if not self.latitude:
            errors['latitude'] = ['Latitude is required.']

        if not self.longitude:
            errors['longitude'] = ['Longitude is required.']

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        if self.team_member_count < 10:
            self.team_member_count = 10
        super().save(*args, **kwargs)
