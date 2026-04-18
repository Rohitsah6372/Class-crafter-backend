
from django.contrib import admin
from django.urls import path
from .views import academic_performance_list_create, location, student_list_create, parent_education_list_create, family_background_list_create, school_list_create, activity_list_create, peer_group_list_create, technology_access_list_create, health

urlpatterns = [

    path('students/', student_list_create, name='student-list-create'),
    path('academic-performance/', academic_performance_list_create, name='academic-performance-list-create'),

    path('parent-education/', parent_education_list_create),
    path('family/', family_background_list_create),
    path('schools/', school_list_create),
    path('activities/', activity_list_create),
    path('peer-groups/', peer_group_list_create),
    path('tech-access/', technology_access_list_create),
    path('health/', health),
    path('location/', location),
]
