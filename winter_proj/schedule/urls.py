from django.urls import path
from . import views

# url configuration
# urlpatterns = [
#     path("hello/", views.say_hello)
# ]
urlpatterns = [
    path("user/", views.create_user, name = 'create user'),
    path("student/", views.create_student, name = 'create_student'),
    path("instructor/", views.create_instructor, name = 'create_instructor'),
    path("create-classes/", views.create_classes, name = 'create_classes'),
    path("get-student-schedule/", views.get_student_timetable, name = 'get_student_timetable'),
    path("get-instructor-schedule/", views.get_instructor_timetable, name = "get_instructor_timetable")
]
