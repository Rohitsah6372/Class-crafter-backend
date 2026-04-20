
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def home(request):
    return HttpResponse("API is running")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('student.urls')),
    path('ml_api/', include('ml_api.urls'), name='predict-student'),
]
