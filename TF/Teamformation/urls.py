from django.contrib import admin
from django.urls import path
from . import views
from .views import collect_user_data,form_teams,get_team_members

urlpatterns = [
   
    path('collect_user_data/', collect_user_data, name='collect_user_data'),
    path('form_teams/', form_teams, name='form_teams'),
    path('api/get_team_members/', get_team_members, name='get_team_members'),
]
