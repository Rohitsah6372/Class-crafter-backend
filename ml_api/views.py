import numpy as np
from django.shortcuts import get_object_or_404, render
from ml_api.services import ai_model, build_features, scaler
from rest_framework.decorators import api_view
from rest_framework.response import Response
from student.models import (AcademicPerformance, Activity, FamilyBackground,
                            Health, Location, ParentEducation, PeerGroup,
                            School, Student, TechnologyAccess)


# Create your views here.
@api_view(['GET'])
def predict_student(request, student_id):
    # return Response({
    #     "message": "Working fine",
    #     "student_id": student_id
    # })


    if not student_id:
        return Response({"error": "Student ID is required"}, status=400)

    student_id = int(student_id)

    if student_id <= 0:
        return Response({"error": "Invalid student ID"}, status=400)
    

    student = Student.objects.filter(id=student_id).first()
    
    
    if not student:
        return Response({"error": "Student not found"}, status=404)


    required_models = {
        "AcademicPerformance": AcademicPerformance,
        "FamilyBackground": FamilyBackground,
        "TechnologyAccess": TechnologyAccess,
        "Health": Health,
        "Location": Location,
    }

    for name, model in required_models.items():
        if not model.objects.filter(student=student).exists():
            return Response({"error": f"{name} data not found"}, status=404)

    if not student.school:
        return Response({"error": "School data not found"}, status=404)

    if not student.peer_group:
        return Response({"error": "Peer group data not found"}, status=404)

    if not student.activities.exists():
        return Response({"error": "Activity data not found"}, status=404)

    student = Student.objects.get(id=student_id) 

    academic = AcademicPerformance.objects.get(student=student)
    family = FamilyBackground.objects.get(student=student)
    school = student.school
    tech = TechnologyAccess.objects.get(student=student)
    health = Health.objects.get(student=student)
    location = Location.objects.get(student=student)

    features = build_features(student, academic, family, school, tech, health, location)

    arr = np.array([features])
    arr = scaler.transform(arr)

    prediction = ai_model.predict(arr)[0]

    return Response({
        "student": {
            "id": student.id,
            "name": getattr(student, "name", None),
            "gender": student.gender
        },

        "academic": {
            "hours_studied": academic.hours_studied,
            "attendance": academic.attendance,
            "previous_scores": academic.previous_scores,
            "tutoring_sessions": academic.tutoring_sessions,
            "motivation_level": academic.motivation_level
        },

        "family": {
            "parental_involvement": family.parental_involvement,
            "family_income": family.family_income,
            "parental_education_level": getattr(family.parent_education, "parental_education_level", 0)
        },

        "school": {
            "teacher_quality": school.teacher_quality,
            "school_type": school.school_type,
            "access_to_resources": school.access_to_resources
        },

        "technology": {
            "internet_access": tech.internet_access
        },

        "health": {
            "physical_activity": health.physical_activity,
            "sleep_hours": health.sleep_hours,
            "learning_disabilities": health.learning_disabilities
        },

        "location": {
            "distance_from_home": location.distance_from_home
        },

        "features_used": features,

        "predicted_score": round(float(prediction), 2)
    })