from django.contrib.auth.models import User
from django.db.models import query

from .models import Course
from rest_framework import viewsets
from rest_framework import permissions
from schooltrackapp.serializers import CourseSerializer, UserSerializer
class UserviewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]
class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    permission_classes=[permissions.IsAuthenticated]
