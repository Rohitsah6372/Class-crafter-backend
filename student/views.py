from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, AcademicPerformance, ParentEducation, FamilyBackground, School, Activity, PeerGroup, TechnologyAccess, Health, Location
from .serializers import StudentSerializer, AcademicPerformanceSerializer, ParentEducationSerializer, FamilyBackgroundSerializer, SchoolSerializer, ActivitySerializer, PeerGroupSerializer, TechnologyAccessSerializer ,HealthSerializer, LocationSerializer


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
    


from .models import AcademicPerformance
from .serializers import AcademicPerformanceSerializer

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
def technology_access_list_create(request):

    if request.method == 'GET':
        data = TechnologyAccess.objects.all()
        serializer = TechnologyAccessSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TechnologyAccessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

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