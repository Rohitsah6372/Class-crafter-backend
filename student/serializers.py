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


from .models import FamilyBackground, ParentEducation

class ParentEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentEducation
        fields = '__all__'


class FamilyBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyBackground
        fields = '__all__'


from .models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'