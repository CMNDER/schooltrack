from django.contrib.auth.models import User
from django.db import models
from .models import Course
from rest_framework import serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields = '__all__'
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
