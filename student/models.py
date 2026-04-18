from django.db import models

class School(models.Model):
    school_type = models.IntegerField()
    access_to_resources = models.IntegerField()
    teacher_quality = models.IntegerField()

    def __str__(self):
        return f"School {self.id}"
    


class Activity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class PeerGroup(models.Model):
    peer_influence = models.IntegerField()

    def __str__(self):
        return f"PeerGroup {self.id}"
    


# Create your models here.
class Student(models.Model):
    gender = models.IntegerField()

    school = models.ForeignKey(
        School,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    activities = models.ManyToManyField(
        Activity,
        blank=True
    )


    peer_group = models.ForeignKey(
    PeerGroup,
    on_delete=models.SET_NULL,
    null=True,
    blank=True
    )

    def __str__(self):
        return f"Student {self.id}"
    






class TechnologyAccess(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    internet_access = models.IntegerField()

    def __str__(self):
        return f"TechAccess {self.student.id}"


    

class AcademicPerformance(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    hours_studied = models.FloatField()
    attendance = models.FloatField()
    previous_scores = models.FloatField()
    tutoring_sessions = models.FloatField()

    def __str__(self):
        return f"AcademicPerformance {self.student.id}"
    

class ParentEducation(models.Model):
    parental_education_level = models.IntegerField()

    def __str__(self):
        return f"Education {self.parental_education_level}"
    

class FamilyBackground(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    family_income = models.IntegerField()
    parental_involvement = models.IntegerField()

    parent_education = models.ForeignKey(
        ParentEducation,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f"FamilyBackground {self.student.id}" 




