from django.urls import include,path
from rest_framework import routers
from .views import CourseViewSet, UserviewSet
router=routers.DefaultRouter()
router.register('users',UserviewSet,'users')
router.register('courses',CourseViewSet)
urlpatterns = router.urls

