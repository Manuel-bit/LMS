from django.contrib import admin
from .models import Student, Tutor

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Student)

class TutorAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Tutor)