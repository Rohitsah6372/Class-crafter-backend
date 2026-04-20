import joblib
import numpy as np
import os
from django.conf import settings


model = joblib.load(settings.MODEL_PATH)
scaler = joblib.load(settings.SCALER_PATH)


def predict(features):

    arr = np.array([features])
    arr = scaler.transform(arr)

    prediction = model.predict(arr)[0]

    return round(float(prediction), 2)



def build_features(student, academic, family, school, tech, health, location):

    return [
        academic.hours_studied or 0.0,
        academic.attendance or 0.0,
        academic.previous_scores or 0.0,
        academic.tutoring_sessions or 0.0,
        academic.motivation_level or 0,

        school.teacher_quality or 0,
        school.school_type or 0,
        location.distance_from_home or 0,

        family.parent_education.parental_education_level if family.parent_education else 0,
        school.access_to_resources or 0,
        tech.internet_access or 0,
        family.family_income or 0,
        family.parental_involvement or 0,

        health.physical_activity or 0.0,
        health.sleep_hours or 0.0,
        health.learning_disabilities or 0,

        student.gender or 0,
        student.peer_group.peer_influence if student.peer_group else 0,
        student.activities.count()
    ]