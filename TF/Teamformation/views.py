from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import UserProfileForm
from .models import UserProfile, Team
from .serializers import UserProfileSerializer, TeamSerializer
import logging



def collect_user_data(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = UserProfileForm()

    return render(request, 'collect_user_data.html', {'form': form})



def form_teams(request):
    target_location = 'dharmapuri'
    target_disaster_type = 'flood'
    team, created = Team.objects.get_or_create(name='Default Team', location=target_location, disaster_type=target_disaster_type)
    # ... your existing logic ...

    if target_disaster_type == 'flood':
        doctors = UserProfile.objects.filter(profession='doctor', location=target_location, disaster_type=target_disaster_type)[:2]
        nurses = UserProfile.objects.filter(profession='nurse', location=target_location, disaster_type=target_disaster_type)[:9]
        police = UserProfile.objects.filter(profession='police', location=target_location, disaster_type=target_disaster_type)[:9]
        ambulance_staff = UserProfile.objects.filter(profession='ambulance', location=target_location, disaster_type=target_disaster_type)[:4]
        team.userprofile_set.set(list(doctors) + list(nurses) + list(ambulance_staff)+ list(police) )
    elif target_disaster_type == 'earthquake':
        doctors = UserProfile.objects.filter(profession='doctor', location=target_location, disaster_type=target_disaster_type)[:2]
        nurses = UserProfile.objects.filter(profession='nurse', location=target_location, disaster_type=target_disaster_type)[:9]
        engineers = UserProfile.objects.filter(profession='engineer', location=target_location, disaster_type=target_disaster_type)[:5]
        ambulance_staff = UserProfile.objects.filter(profession='ambulance', location=target_location, disaster_type=target_disaster_type)[:4]
        police = UserProfile.objects.filter(profession='police', location=target_location, disaster_type=target_disaster_type)[:9]
        rescue_workers = UserProfile.objects.filter(profession='rescue_worker', location=target_location, disaster_type=target_disaster_type)[:7]
        team.userprofile_set.set(list(engineers) + list(rescue_workers) + list(ambulance_staff)+list(doctors) + list(nurses)+ list(police) )
    elif target_disaster_type == 'landslide':
        # Allocate teams differently for landslide
        # Example: Allocate more geologists and construction workers
        doctors = UserProfile.objects.filter(profession='doctor', location=target_location, disaster_type=target_disaster_type)[:2]
        nurses = UserProfile.objects.filter(profession='nurse', location=target_location, disaster_type=target_disaster_type)[:9]
        geologists = UserProfile.objects.filter(profession='geologist', location=target_location, disaster_type=target_disaster_type)[:2]
        police = UserProfile.objects.filter(profession='police', location=target_location, disaster_type=target_disaster_type)[:9]
        construction_workers = UserProfile.objects.filter(profession='construction_worker', location=target_location, disaster_type=target_disaster_type)[:8]
        ambulance_staff = UserProfile.objects.filter(profession='ambulance', location=target_location, disaster_type=target_disaster_type)[:4]
        team.userprofile_set.set(list(geologists) + list(construction_workers)+list(doctors) + list(nurses)+ list(ambulance_staff)+ list(police))
    else:
        # Your default allocation logic for other disaster types
        eligible_team_members = UserProfile.objects.filter(location=target_location, disaster_type=target_disaster_type)
        team, created = Team.objects.get_or_create(name='Default Team', location=target_location, disaster_type=target_disaster_type)
        team.userprofile_set.set(eligible_team_members)

    return render(request, 'display_team.html', {'team_members': team.userprofile_set.all()})

   

@api_view(['GET'])
def get_team_members(request):
    # Specify the target location and disaster type
    target_location = 'dharmapuri'
    target_disaster_type = 'earthquake'
    
    # Create or retrieve the team
    team, created = Team.objects.get_or_create(name='Default Team', location=target_location, disaster_type=target_disaster_type)

    if target_disaster_type == 'flood':
        # Allocate teams differently for flood
        # Example: Allocate more doctors and nurses
        doctors = UserProfile.objects.filter(profession='doctor', location=target_location, disaster_type=target_disaster_type)[:2]
        nurses = UserProfile.objects.filter(profession='nurse', location=target_location, disaster_type=target_disaster_type)[:9]
        ambulance_staff = UserProfile.objects.filter(profession='ambulance', location=target_location, disaster_type=target_disaster_type)[:4]
        team.userprofile_set.set(list(doctors) + list(nurses) + list(ambulance_staff))
    elif target_disaster_type == 'earthquake':
        doctors = UserProfile.objects.filter(profession='doctor', location=target_location, disaster_type=target_disaster_type)[:2]
        nurses = UserProfile.objects.filter(profession='nurse', location=target_location, disaster_type=target_disaster_type)[:9]
        ambulance_staff = UserProfile.objects.filter(profession='ambulance', location=target_location, disaster_type=target_disaster_type)[:4]
        engineers = UserProfile.objects.filter(profession='engineer', location=target_location, disaster_type=target_disaster_type)[:5]
        police = UserProfile.objects.filter(profession='police', location=target_location, disaster_type=target_disaster_type)[:9]
        rescue_workers = UserProfile.objects.filter(profession='rescue_worker', location=target_location, disaster_type=target_disaster_type)[:7]
        team.userprofile_set.set(list(engineers) + list(rescue_workers) +list(doctors) + list(nurses) +list(ambulance_staff)+list(police))
        pass
    elif target_disaster_type == 'landslide':
        doctors = UserProfile.objects.filter(profession='doctor', location=target_location, disaster_type=target_disaster_type)[:2]
        nurses = UserProfile.objects.filter(profession='nurse', location=target_location, disaster_type=target_disaster_type)[:9]
        geologists = UserProfile.objects.filter(profession='geologist', location=target_location, disaster_type=target_disaster_type)[:2]
        construction_workers = UserProfile.objects.filter(profession='construction_worker', location=target_location, disaster_type=target_disaster_type)[:8]
        team.userprofile_set.set(list(geologists) + list(construction_workers)+list(doctors) + list(nurses))
        pass
    else:
        # Your default allocation logic for other disaster types
        eligible_team_members = UserProfile.objects.filter(location=target_location, disaster_type=target_disaster_type)
        team.userprofile_set.set(eligible_team_members)

    # Update UserProfile objects to link them to the team
    UserProfile.objects.filter(id__in=team.userprofile_set.values_list('id', flat=True)).update(team=team)

    # Retrieve and serialize team members
    team_members = team.userprofile_set.all()
    serializer = UserProfileSerializer(team_members, many=True)

    return Response(serializer.data)
