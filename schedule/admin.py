from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import (
    Student, Instructor, TPO, Schedule, Classes,
    TechPerformance, HRPerformance, GD_ExtemporePerformance
)

User = get_user_model()

# Register User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)


# Register Schedule model
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')


# Register Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'batch_name', 'rtu_roll_no')
    search_fields = ('get_username', 'roll_number')
    list_filter = ('branch', 'phase')

    def get_username(self, obj):
        return obj.student.username  # Access related user model's username
    get_username.short_description = 'Username'


# Register Instructor model
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email')
    search_fields = ('get_username', 'get_email')

    def get_username(self, obj):
        return obj.instructor.username  # Access related user model's username
    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.instructor.email  # Access related user model's email
    get_email.short_description = 'Email'


# Register TPO model
@admin.register(TPO)
class TPOAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email')
    search_fields = ('get_username', 'get_email')

    def get_username(self, obj):
        return obj.tpo.username  # Access related user model's username
    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.tpo.email  # Access related user model's email
    get_email.short_description = 'Email'


# Register Classes model
@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'batch_name', 'phase', 'date', 'start_time', 'end_time')
    search_fields = ('class_name', 'batch_name', 'phase')
    list_filter = ('date', 'phase')


# Register TechPerformance model
@admin.register(TechPerformance)
class TechPerformanceAdmin(admin.ModelAdmin):
    list_display = ('get_student_name', 'score', 'remark')
    search_fields = ('get_student_name',)
    list_filter = ('score',)

    def get_student_name(self, obj):
        return obj.student.student_name  # Assuming student has a field 'student_name'
    get_student_name.short_description = 'Student Name'


# Register HRPerformance model
@admin.register(HRPerformance)
class HRPerformanceAdmin(admin.ModelAdmin):
    list_display = ('get_student_name', 'score', 'remark')
    search_fields = ('get_student_name',)
    list_filter = ('score',)

    def get_student_name(self, obj):
        return obj.student.student_name
    get_student_name.short_description = 'Student Name'


# Register GD_ExtemporePerformance model
@admin.register(GD_ExtemporePerformance)
class GD_ExtemporePerformanceAdmin(admin.ModelAdmin):
    list_display = ('get_student_name', 'score', 'remark')
    search_fields = ('get_student_name',)
    list_filter = ('score',)

    def get_student_name(self, obj):
        return obj.student.student_name
    get_student_name.short_description = 'Student Name'
