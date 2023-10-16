from django.urls import path
from . import views 
from  django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    #reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #Registration
    path('register/', views.register, name='register'),
    path('org_registration/', views.organization_registration, name='org_registration'),
   # path('user_location/', views.user_location, name='user_location'),
    path('org-loc/', views.organization_locations_map, name='org_loc'),
    path('location_input/', views.location_input, name='location_input'),
    path('success/', views.success, name='success'),
    path('home', views.home, name='home'),
]