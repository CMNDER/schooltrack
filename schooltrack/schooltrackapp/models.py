from django.db import models
from django.conf import settings
# Create your models here.
course_status = (
    ('CURRENT', 'CURRENTLY UNDERTAKEN'),
    ('COMPLETED', 'COMPLETED'),
)

class Course(models.Model):
    course_name = models.CharField(max_length=200, blank=False, null=False)
    course_code = models.CharField(
        max_length=10, unique=True, blank=False, null=False)
    course_credits = models.IntegerField(null=False, blank=False)
    course_registration_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.course_name


class CompletedCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_of_completion = models.DateField(
        auto_created=True, blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

class CurrentUndertakenCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(choices=course_status, max_length=20)
    date_of_course_registration = models.DateField(auto_created=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
