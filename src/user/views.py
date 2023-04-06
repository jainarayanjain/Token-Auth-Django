import json

from django.core.serializers import serialize
from django.http import JsonResponse

from user.models import EmployeeDetails
from user.serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class GetRequest(viewsets.ModelViewSet):

    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeSerializer

