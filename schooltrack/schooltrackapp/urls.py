from django.urls import include,path
from rest_framework import routers
from .api import CourseViewSet
router=routers.DefaultRouter()
router.register('courses',CourseViewSet)
urlpatterns = router.urls

