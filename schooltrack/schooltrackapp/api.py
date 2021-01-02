from django.contrib.auth.models import User
from django.db.models import query

from .models import Course
from rest_framework import viewsets
from rest_framework import permissions
from schooltrackapp.serializers import  CourseSerializer
from rest_framework import  permissions


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CourseSerializer


class CurrentCourseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.request.user.currentundertakencourse.all()

    def perform_create(self, serializer):
        serializer.save()
