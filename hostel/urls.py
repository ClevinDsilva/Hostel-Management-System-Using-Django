from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),


    # Admin URLs
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
    path('view_complaints/', views.view_complaints, name='view_complaints'),

    # Student URLs
    path('view_students/', views.view_students, name='view_students'),
    path('add_student/', views.add_student, name='add_student'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),

    # Employee URLs
    path('view_employees/', views.view_employees, name='view_employees'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),

    # Room URLs
    path('view_rooms/', views.view_rooms, name='view_rooms'),
    path('add_room/', views.add_room, name='add_room'),
    path('update_room/<int:room_id>/', views.update_room, name='update_room'),
    path('delete_room/<int:room_id>/', views.delete_room, name='delete_room'),

    path('view_mess_details/', views.view_mess_details, name='view_mess_details'),
    path('add_mess_details/<str:day>/', views.add_mess_details, name='add_mess_details'),
    path('edit_mess_details/<int:pk>/', views.edit_mess_details, name='edit_mess_details'),
    path('delete_mess_details/<int:pk>/', views.delete_mess_details, name='delete_mess_details'),

    # Warden URLs
    path('warden_login/', views.warden_login, name='warden_login'),
    path('warden_dashboard/', views.warden_dashboard, name='warden_dashboard'),
    path('add_warden/', views.add_warden, name='add_warden'),
    path('view_wardens/', views.view_wardens, name='view_wardens'),
    path('update_warden/<int:warden_id>/', views.update_warden, name='update_warden'),
    path('delete_warden/<int:warden_id>/', views.delete_warden, name='delete_warden'),

   # Student URLs
    path('student_login/', views.student_login, name='student_login'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('view_mess_details/', views.view_mess_details, name='view_mess_details'),
    path('view_mess_items/', views.view_mess_items, name='view_mess_items'),
    path('view_roommates/', views.view_roommates, name='view_roommates'),
    path('raise_complaint/', views.raise_complaint, name='raise_complaint'),
]
