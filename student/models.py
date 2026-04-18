from django.db import models

# Create your models here.
class Student(models.Model):
    gender = models.IntegerField()

    def __str__(self):
        return f"Student {self.id}"