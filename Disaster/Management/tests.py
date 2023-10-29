from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Organization

class OrganizationApiTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

    def test_organization_registration(self):
        url = reverse('register-organization')
        data = {
            "Organization_name": "Test Org",
            "Organization_type": "Type A",
            "address": "123 Test St",
            "phone_number": "123-456-7890",
            "admin_name": self.user.id,
            "team_member_count": 10,
            "Organization_location": "Test Location",
            "latitude": 40.7128,
            "longitude": -74.0060
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_organization_locations_map(self):
        url = reverse('organization-locations')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class OrganizationViewTests(TestCase):
    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/home.html')

    def test_organization_registration_view(self):
        response = self.client.get(reverse('organization-registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/org_registration.html')

    def test_location_input_view(self):
        response = self.client.get(reverse('location-input'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'geo_location.html')

    def test_success_view(self):
        response = self.client.get(reverse('success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success.html')

