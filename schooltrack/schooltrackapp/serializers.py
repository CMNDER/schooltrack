from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
