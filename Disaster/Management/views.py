from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Organization
from .serializers import OrganizationSerializer

@api_view(['GET','POST','PUT','DELETE'])
def get_organization_locations(request,id):
    if request.method=="GET":
       organizations = Organization.objects.all()
       serializer = OrganizationSerializer(organizations, many=True)
       return Response(serializer.data)
    
    elif request.method=="POST":
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({'message': 'Organization registered successfully'})
        return Response(serializer.errors, status=400)

    elif request.method == "PUT":
        Organizationid = request.data.get('id') 
        try:
            organization = Organization.objects.get(Organizationid=id)
        except Organization.DoesNotExist:
            return Response({'message': 'Organization not found'}, status=404)

        serializer = OrganizationSerializer(organization, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Organization updated successfully'})
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        Organizationid = request.data.get('id')  
        try:
            organization = Organization.objects.get(Organizationid=id)
        except Organization.DoesNotExist:
            return Response({'message': 'Organization not found'}, status=404)

        organization.delete()
        return Response({'message': 'Organization deleted successfully'})

    return Response({'message': 'Invalid HTTP method'}, status=405)




"""from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Management.forms import UserRegistrationForm  # Adjust the import if needed
from .forms import OrganizationForm
from django.http import JsonResponse
from .models import Organization

@login_required
def dashboard(request):
    return render(request, 'registration/home.html', {'section': 'home'})

def organization_locations_map(request):
    # Retrieve organization locations from the Organization model
    organizations = Organization.objects.filter(latitude__isnull=False, longitude__isnull=False)

    return render(request, 'registration/home.html', {'organizations': organizations})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistartionForm(request.POST)
        if user_form.is_valid():
            #Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            #Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            #Save the user object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
        
    else:
        user_form = UserRegistartionForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

def register(request):
    
    # Check if the user is already authenticated (logged in)
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the user object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def organization_registration(request):
    if request.method == 'POST':
        org_form = OrganizationForm(request.POST)
        if org_form.is_valid():
            organization = org_form.save(commit=False)

            # Check if all required fields are provided
            if all([organization.Organization_name, organization.Organization_type, organization.address,
                    organization.phone_number,organization.admin_name, organization.team_member_count, organization.Organization_location, 
                    organization.latitude, organization.longitude]):
                # Save the organization object with all the data
                organization.save()
                # You can add additional logic here if needed
                return redirect('home')  # Redirect to the success page after successful registration

    else:
        org_form = OrganizationForm()

    return render(request, 'registration/org_registration.html', {'org_form': org_form})

#def store_user_location(request):
 #   if request.method == 'POST':
        # Parse the latitude and longitude values from the POST request
  #      latitude = request.POST.get('latitude')
   #     longitude = request.POST.get('longitude')

        # Retrieve the user's organization (modify this part based on your logic)
    #    organization = Organization.objects.get(admin_name=request.user)
   # Update the organization's latitude and longitude
     #   organization.latitude = latitude
      #  organization.longitude = longitude
       # organization.save()

        #return JsonResponse({'message': 'Location stored successfully.'})
    #else:
     #   return JsonResponse({'message': 'Invalid request.'}, status=400)

def location_input(request):
    return render(request, 'geo_location.html')

def success(request):
    return render(request, 'success.html')

def home(request):
    return render(request, 'registration/home.html')



def home(request):
    # Query the database to get organizations with valid latitude and longitude
    organizations = Organization.objects.filter(latitude__isnull=False, longitude__isnull=False)

    # Create a list of dictionaries with latitude and longitude
    organization_data = [{'latitude': org.latitude, 'longitude': org.longitude} for org in organizations]

    return render(request, 'registration/home.html', {'organization_data': organization_data})



"""

