from rest_framework import serializers
from .models import Student, AcademicPerformance, ParentEducation, FamilyBackground, School, Activity, PeerGroup, TechnologyAccess

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



class AcademicPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicPerformance
        fields = '__all__'



class ParentEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentEducation
        fields = '__all__'


class FamilyBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyBackground
        fields = '__all__'



class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'



class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        


class PeerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeerGroup
        fields = '__all__'


class TechnologyAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyAccess
        fields = '__all__'