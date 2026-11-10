from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('details_us/', views.student_details, name='details'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
   path(
    'students/update/<int:id>/',
    views.update_student,
    name='update_student'
),
path(
    'students/delete/<int:id>/',
    views.delete_student,
    name='delete_student'
),
path('dashboard/', views.dashboard, name='dashboard'),
]