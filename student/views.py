from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (AcademicPerformance, Activity, FamilyBackground, Health,
                     Location, ParentEducation, PeerGroup, School, Student,
                     TechnologyAccess)
from .serializers import (AcademicPerformanceSerializer, ActivitySerializer,
                          FamilyBackgroundSerializer, HealthSerializer,
                          LocationSerializer, ParentEducationSerializer,
                          PeerGroupSerializer, SchoolSerializer,
                          StudentSerializer, TechnologyAccessSerializer)


@api_view(['GET', 'POST'])
def student_list_create(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

@api_view(['GET'])
def get_all_details(request, student_id):

    student = Student.objects.filter(id=student_id).first()
    if not student:
        return Response({"error": "Student not found"}, status=404)
    
    academic = AcademicPerformance.objects.filter(student=student).first()
    family = FamilyBackground.objects.filter(student=student).first()
    tech = TechnologyAccess.objects.filter(student=student).first()
    health = Health.objects.filter(student=student).first()
    location = Location.objects.filter(student=student).first()

    data = {
        "student": StudentSerializer(student).data,

        "academic": {
            "hours_studied": getattr(academic, "hours_studied", 0),
            "attendance": getattr(academic, "attendance", 0),
            "previous_scores": getattr(academic, "previous_scores", 0),
            "tutoring_sessions": getattr(academic, "tutoring_sessions", 0),
            "motivation_level": getattr(academic, "motivation_level", 0),
        },

        "family": {
            "parental_involvement": getattr(family, "parental_involvement", 0),
            "family_income": getattr(family, "family_income", 0),
        },

        "technology": {
            "internet_access": getattr(tech, "internet_access", 0),
        },

        "health": {
            "physical_activity": getattr(health, "physical_activity", 0),
            "sleep_hours": getattr(health, "sleep_hours", 0),
            "learning_disabilities": getattr(health, "learning_disabilities", 0),
        },

        "location": {
            "distance_from_home": getattr(location, "distance_from_home", 0),
        },
    }

    return Response(data)


@api_view(['PUT','PATCH'])    
def student_list_update(request, student_id):

    student = Student.objects.filter(id=student_id).first()
    if not student:
        return Response({"error": "Student not found"}, status=404)

    data = request.data

    student_data = data.get("student", {})
    for key, value in student_data.items():
        setattr(student, key, value)
    student.save()

    academic_data = data.get("academic", {})
    if academic_data:
        academic, _ = AcademicPerformance.objects.get_or_create(student=student)
        for key, value in academic_data.items():
            setattr(academic, key, value)
        academic.save()

    family_data = data.get("family", {})
    if family_data:
        family, _ = FamilyBackground.objects.get_or_create(student=student)
        for key, value in family_data.items():
            setattr(family, key, value)
        family.save()

    tech_data = data.get("technology", {})
    if tech_data:
        tech, _ = TechnologyAccess.objects.get_or_create(student=student)
        for key, value in tech_data.items():
            setattr(tech, key, value)
        tech.save()

    health_data = data.get("health", {})
    if health_data:
        health, _ = Health.objects.get_or_create(student=student)
        for key, value in health_data.items():
            setattr(health, key, value)
        health.save()

    location_data = data.get("location", {})
    if location_data:
        location, _ = Location.objects.get_or_create(student=student)
        for key, value in location_data.items():
            setattr(location, key, value)
        location.save()

    return Response({"message": "Student data updated successfully"})


@api_view(['DELETE'])
def student_delete(request, student_id):

    student = Student.objects.filter(id=student_id).first()
    if not student:
        return Response({"error": "Student not found"}, status=404)

    student.delete()
    return Response({"message": "Student deleted successfully"})


@api_view(['GET', 'POST'])
def academic_performance_list_create(request):

    if request.method == 'GET':
        data = AcademicPerformance.objects.all()
        serializer = AcademicPerformanceSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AcademicPerformanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

@api_view(['GET', 'POST'])
def parent_education_list_create(request):

    if request.method == 'GET':
        data = ParentEducation.objects.all()
        serializer = ParentEducationSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ParentEducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    


@api_view(['GET', 'POST'])
def family_background_list_create(request):

    if request.method == 'GET':
        data = FamilyBackground.objects.all()
        serializer = FamilyBackgroundSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FamilyBackgroundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

@api_view(['GET', 'POST'])
def school_list_create(request):

    if request.method == 'GET':
        data = School.objects.all()
        serializer = SchoolSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET'])
def getschool_detail(request, school_id):
    school = School.objects.filter(id=school_id).first()
    if not school:
        return Response({"error": "School not found"}, status=404)
    serializer = SchoolSerializer(school)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def activity_list_create(request):

    if request.method == 'GET':
        data = Activity.objects.all()
        serializer = ActivitySerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

@api_view(['GET', 'POST'])
def peer_group_list_create(request):

    if request.method == 'GET':
        data = PeerGroup.objects.all()
        serializer = PeerGroupSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PeerGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

@api_view(['GET', 'POST'])
def technology_access_list_create(request, student_id=None):

    if request.method == 'GET':
        if student_id:
            data = TechnologyAccess.objects.filter(student_id=student_id)
        else:
            data = TechnologyAccess.objects.all()

        serializer = TechnologyAccessSerializer(data, many=True)
        return Response(serializer.data)
    
    

    if request.method == 'POST':

        # ? Ensure student_id is provided
        if not student_id:
            return Response(
                {"error": "student_id is required in URL"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ? Check if student exists
        student = get_object_or_404(Student, id=student_id)

        # ? Prevent duplicate (OneToOne)
        if TechnologyAccess.objects.filter(student=student).exists():
            return Response(
                {"error": "TechnologyAccess already exists for this student"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Attach student
        data = request.data.copy()
        data['student'] = student.id

        serializer = TechnologyAccessSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def health(request):

    if request.method == 'GET':
        data = Health.objects.all()
        serializer = HealthSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = HealthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

@api_view(['GET', 'POST'])
def location(request):

    if request.method == 'GET':
        data = Location.objects.all()
        serializer = LocationSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)