
from django.contrib import admin
from django.urls import include, path
from ml_api.views import predict_student

urlpatterns = [
    path('predicts/<int:student_id>/', predict_student),
]
