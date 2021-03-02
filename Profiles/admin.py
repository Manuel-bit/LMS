from django.contrib import admin
from .models import Student, Tutor, Course, Unit, Notes

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Student)

class TutorAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Tutor)

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Course)

class UnitAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Unit)

class NoteAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Notes)