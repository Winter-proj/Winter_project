from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import (
    Student, Instructor, TPO, Schedule, Classes, 
    TechPerformance, HRPerformance, GD_ExtemporePerformance
)

User = get_user_model()
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student__username', 'batch_name', 'rtu_roll_no')
    search_fields = ('student__username', 'roll_number')
    list_filter = ('branch', 'phase')

# Register Instructor model
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('instructor__username', 'instructor__email')
    search_fields = ('instructor__username', 'instructor__email')

# Register TPO model
@admin.register(TPO)
class TPOAdmin(admin.ModelAdmin):
    list_display = ('tpo__username', 'tpo__email')
    search_fields = ('tpo__username', 'tpo__email')

# Register Classes model
@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'batch_name', 'phase', 'date', 'start_time', 'end_time')
    search_fields = ('class_name', 'batch_name', 'phase')
    list_filter = ('date', 'phase')

# Register TechPerformance model
@admin.register(TechPerformance)
class TechPerformanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'score', 'remark')
    search_fields = ('student__student_name',)
    list_filter = ('score',)

# Register HRPerformance model
@admin.register(HRPerformance)
class HRPerformanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'score', 'remark')
    search_fields = ('student__student_name',)
    list_filter = ('score',)

# Register GD_ExtemporePerformance model
@admin.register(GD_ExtemporePerformance)
class GD_ExtemporePerformanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'score', 'remark')
    search_fields = ('student__student_name',)
    list_filter = ('score',)
