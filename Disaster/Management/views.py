from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Management.forms import UserRegistrationForm  # Adjust the import if needed
from .forms import OrganizationForm
from django.http import JsonResponse
from .models import Organization

@login_required
def dashboard(request):
    return render(request, 'registration/home.html', {'section': 'home'})

def organization_locations_map(request):
    
    organizations = Organization.objects.filter(latitude__isnull=False, longitude__isnull=False)

    return render(request, 'registration/home.html', {'organizations': organizations})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistartionForm(request.POST)
        if user_form.is_valid():
          
            new_user = user_form.save(commit=False)
         
            new_user.set_password(
                user_form.cleaned_data['password'])
     
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
        
    else:
        user_form = UserRegistartionForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

def register(request):
    
  
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            
            new_user = user_form.save(commit=False)
           
            new_user.set_password(user_form.cleaned_data['password'])
   
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

            
            if all([organization.Organization_name, organization.Organization_type, organization.address,
                    organization.phone_number,organization.admin_name, organization.team_member_count, organization.Organization_location, 
                    organization.latitude, organization.longitude]):
                
                organization.save()
                
                return redirect('home')  

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
    organizations = Organization.objects.all()
    return render(request, 'registration/home.html', {'organizations': organizations})





