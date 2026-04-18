from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


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