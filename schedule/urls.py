from django.urls import path
from . import views

# url configuration
# urlpatterns = [
#     path("hello/", views.say_hello)
# ]

urlpatterns = [
    
    path('user/create/api/', views.create_user, name='create_user'),
    path('instructor/create/api/', views.create_instructor, name='create_instructor'),
    path('student/create/api/', views.create_student, name = 'create_student'),
    path('schedule/create/api/', views.create_schedule, name='create_schedule'),
    path('classes/create/api/', views.create_classes, name='create_classes'),
    path('tpo/create/api/', views.create_TPO, name='create _tpo'),

    path('user/create/form', views.user_view, name='user_form'),
    path('instructor/create/form', views.instructor_view, name='instructor_form'),
    path('student/create/form', views.student_view, name = 'student_form'),
    path('schedule/create/form', views.schedule_view, name='schedule_form'),
    path('classes/create/form', views.class_view, name='classes_form'),
    path('tpo/create/form', views.tpo_view, name='tpo_form'),

    path('schedule/view/<str:class_id>/', views.view_class_timetable, name= 'view_class_timetable'),

    path('', views.ClassesGetCreate.as_view()),
    path('<str:class_id>/', views.ClassesGetRetrieveUpdateDestroy.as_view())
    # path('event/<int:event_id>/', views.get_event, name='get_event'),
    # path('instructor/<int:instructor_id>/timetable/', views.get_instructor_timetable, name='get_instructor_timetable'),
    # path('student/<int:student_id>/timetable/', views.get_student_timetable, name='get_student_timetable')
]

