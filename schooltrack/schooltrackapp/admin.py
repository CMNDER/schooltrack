from django.contrib import admin
from .models import Course,CompletedCourse,CurrentUndertakenCourse
# Register your models here.
admin.site.register(Course)
admin.site.register(CurrentUndertakenCourse)
admin.site.register(CompletedCourse)