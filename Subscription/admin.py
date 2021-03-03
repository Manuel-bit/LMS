from django.contrib import admin
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Course)

