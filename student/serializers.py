from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


from .models import AcademicPerformance

class AcademicPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicPerformance
        fields = '__all__'