from django.urls import path
from . import views 
#from  django.contrib.auth import views as auth_views


urlpatterns = [
    path('api/organization-locations/<str:id>', views.get_organization_locations, name='organization-locations'),
   # path('api/register-organization/', views.register_organization, name='register-organization'),
  
]