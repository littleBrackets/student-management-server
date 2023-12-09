from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SignupSerializer, SchoolSerializer
from .models import SignUP, School

# Create your views here.

class SignupView(viewsets.ModelViewSet):
    serializer_class = SignupSerializer
    queryset = SignUP.objects.all()

class SchoolView(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()