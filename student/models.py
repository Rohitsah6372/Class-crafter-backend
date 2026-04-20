from django.db import models


class School(models.Model):

    class SchoolType(models.IntegerChoices):
        PUBLIC = 1, "Public"
        PRIVATE = 2, "Private"
        GOVERNMENT_AIDED = 3, "Government Aided"
        
    school_type = models.IntegerField(choices=SchoolType.choices, null=False, blank=False)
    school_name = models.CharField(max_length=100, null=False, blank=False, default="ABC School")
    access_to_resources = models.IntegerField(null=True, blank=True)
    
    class TeacherQuality(models.IntegerChoices):
        LOW = 1, "Below Average"
        MEDIUM = 2, "Average"
        HIGH = 3, "Above Average"
        VERY_HIGH = 4, "Excellent"
    
    teacher_quality = models.IntegerField(choices=TeacherQuality.choices, null=False, blank=False)

    def __str__(self):
        return f"School {self.id}"
    

class Activity(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class PeerGroup(models.Model):
    peer_influence = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"PeerGroup {self.id}"
    

# Create your models here.
class Student(models.Model):
    class GenderType(models.IntegerChoices):
        MALE = 1, "Male"
        FEMALE = 2, "Female"
        OTHER = 3, "Other"  
            
    gender = models.IntegerField(choices=GenderType.choices, null=False, blank=False)

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

    class InternetAccess(models.IntegerChoices):
        NONE = 1, "No Access"
        LIMITED = 2, "Limited Access"
        FULL = 3, "Full Access"

    internet_access = models.IntegerField(choices=InternetAccess.choices, null=False, blank=False)

    def __str__(self):
        return f"TechAccess {self.student.id}"


class AcademicPerformance(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    class StudyHours(models.IntegerChoices):
        ZERO = 1, "0 hours"
        ONE_TO_TWO = 2, "1-2 hours"
        THREE_TO_FOUR = 3, "3-4 hours"
        FIVE_OR_MORE = 4, "5 or more hours"
        

    hours_studied = models.IntegerField(choices=StudyHours.choices, null=True, blank=True)

    class Attendance(models.IntegerChoices):
        LOW = 1, "Low"
        MEDIUM = 2, "Medium"
        HIGH = 3, "High"
            
    attendance = models.IntegerField(choices=Attendance.choices, null=True, blank=True)
    
    previous_scores = models.FloatField()
    
    class TutoringSessions(models.IntegerChoices):
        NONE = 1, "No Sessions"
        FEW = 2, "1-2 Sessions"
        SOME = 3, "3-4 Sessions"
        MANY = 4, "5 or more Sessions"
    
    tutoring_sessions = models.IntegerField(choices=TutoringSessions.choices, null=True, blank=True)
    
    class MotivationLevel(models.IntegerChoices):
        LOW = 1, "Low"
        MEDIUM = 2, "Medium"
        HIGH = 3, "High"
        VERY_HIGH = 4, "Very High"
    
    motivation_level = models.IntegerField(choices=MotivationLevel.choices, default=MotivationLevel.MEDIUM, null=True, blank=True)

    def __str__(self):
        return f"AcademicPerformance {self.student.id}"
    

class ParentEducation(models.Model):
    
    class EducationLevel(models.IntegerChoices):
        NONE = 1, "No Formal Education"
        PRIMARY = 2, "Primary Education"
        SECONDARY = 3, "Secondary Education"
        HIGHER = 4, "Higher Education"
    
    parental_education_level = models.IntegerField(choices=EducationLevel.choices, null=False, blank=False)

    def __str__(self):
        return f"Education {self.parental_education_level}"
    

class FamilyBackground(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    class IncomeLevel(models.IntegerChoices):
        LOW = 1, "Low Income"
        MEDIUM = 2, "Medium Income"
        HIGH = 3, "High Income"

    family_income = models.IntegerField(choices=IncomeLevel.choices, null=False, blank=False )
    
    class ParentalInvolvement(models.IntegerChoices):
        LOW = 1, "Low Involvement"
        MEDIUM = 2, "Medium Involvement"
        HIGH = 3, "High Involvement"
    
    parental_involvement = models.IntegerField(choices=ParentalInvolvement.choices, null=True, blank=True)

    parent_education = models.ForeignKey(
        ParentEducation,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f"FamilyBackground {self.student.id}" 


class Health(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    class PhysicalActivity(models.IntegerChoices):
        LOW = 1, "Low"
        MEDIUM = 2, "Medium"
        HIGH = 3, "High"

    physical_activity = models.IntegerField(choices=PhysicalActivity.choices, null=True, blank=True)
    
    class SleepHours(models.IntegerChoices):
        ZERO = 1, "0 hours"
        ONE_TO_TWO = 2, "1-2 hours"
        THREE_TO_FOUR = 3, "3-4 hours"
        FIVE_OR_MORE = 4, "5 or more hours"
    
    sleep_hours = models.IntegerField(choices=SleepHours.choices, null=True, blank=True)
    
    class LearningDisabilitis(models.IntegerChoices):
        YES = 1, "Yes"
        NO = 2, "No"
    
    
    learning_disabilities = models.IntegerField(choices=LearningDisabilitis.choices, null=True, blank=True)


class Location(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    class Distance(models.IntegerChoices):
        NEAR = 1, "Near"
        FAR = 2, "Far"

    distance_from_home = models.IntegerField(choices=Distance.choices, null=False, blank=False)



