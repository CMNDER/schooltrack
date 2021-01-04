from schooltrackapp.models import Course
from rest_framework import viewsets, permissions
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CourseSerializer

    def get_queryset(self):
        return self.request.user.courses.all()
    def perform_create(self, serializer):
        print("Here is the request"+ self.request)
        serializer.save(student=self.request.user)
