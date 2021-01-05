from django.contrib import admin
from .models import Course, CompletedCourse, CurrentUndertakenCourse, Semester
# Register your models here.
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(CurrentUndertakenCourse)
admin.site.register(CompletedCourse)
