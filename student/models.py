from django.db import models

# Create your models here.
class Student(models.Model):
    gender = models.IntegerField()

    def __str__(self):
        return f"Student {self.id}"
    

class AcademicPerformance(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    hours_studied = models.FloatField()
    attendance = models.FloatField()
    previous_scores = models.FloatField()
    tutoring_sessions = models.FloatField()

    def __str__(self):
        return f"AcademicPerformance {self.student.id}"