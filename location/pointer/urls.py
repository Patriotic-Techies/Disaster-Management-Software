from django.urls import path
from .views import register_organization, get_organizations, save_user_location, get_user_locations

urlpatterns = [
    path('api/register_organization/', register_organization, name='register_organization'),
    path('api/get_organizations/', get_organizations, name='get_organizations'),
    path('api/save_user_location/', save_user_location, name='save_user_location'),
    path('api/get_user_locations/', get_user_locations, name='get_user_locations'),
    # Other URL patterns
]
