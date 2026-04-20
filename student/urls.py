
from django.contrib import admin
from django.urls import path
from ml_api.views import predict_student

from .views import (academic_performance_list_create, activity_list_create,
                    family_background_list_create, get_all_details,
                    getschool_detail, health, location,
                    parent_education_list_create, peer_group_list_create,
                    school_list_create, student_delete, student_list_create,
                    student_list_update, technology_access_list_create)

urlpatterns = [

    path('students/', student_list_create, name='student-list-create'),
    path('students/update/<int:student_id>/', student_list_update, name='student-update'),
    path('students/delete/<int:student_id>/', student_delete, name='student-delete'),
    path('students/<int:student_id>/', get_all_details, name='student-detail'),
                                                                                                        
    
    
    path('academic-performance/', academic_performance_list_create, name='academic-performance-list-create'),

    path('parent-education/', parent_education_list_create),
    path('family/', family_background_list_create),
    
    
    path('schools/', school_list_create),
    path('schools/<int:school_id>/', getschool_detail),
    
    
    path('activities/', activity_list_create),
    path('peer-groups/', peer_group_list_create),
    path('tech-access/', technology_access_list_create),
    path('health/', health),
    path('location/', location),
    path('predict/<int:student_id>/', predict_student),
]
