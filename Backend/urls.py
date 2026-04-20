
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse



def home(request):
    return HttpResponse("API is running")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('student.urls')),
]
