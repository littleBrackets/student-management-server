from rest_framework import serializers
from .models import SignUP, School

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUP
        fields = ('idx', 'username', 'password')

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('idx', 'name', 'email', 'address', 'contact')