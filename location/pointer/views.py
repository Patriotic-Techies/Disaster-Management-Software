# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Organization
from .serializers import OrganizationSerializer
from django.http import JsonResponse
from .models import UserLocation
from .serializers import UserLocationSerializer

@api_view(['POST'])
def save_user_location(request):
    serializer = UserLocationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def get_user_locations(request):
    user_locations = UserLocation.objects.all()
    serializer = UserLocationSerializer(user_locations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    


@api_view(['POST'])
def register_organization(request):
    serializer = OrganizationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET function for retrieving organization data
@api_view(['GET'])
def get_organizations(request):
    organizations = Organization.objects.all()
    serializer = OrganizationSerializer(organizations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)