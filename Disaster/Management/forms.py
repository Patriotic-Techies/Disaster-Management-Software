from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Organization

class LoginForm(forms.Form):
    username = forms.CharField()
    organization_name = forms.CharField(max_length=100, label='Organization Name')
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Check if the username is already in use
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already in use. Please choose a different one.")

        return username

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['Organization_name', 'Organization_type', 'address', 'phone_number', 'admin_name', 'team_member_count', 'Organization_location', 'latitude', 'longitude']
