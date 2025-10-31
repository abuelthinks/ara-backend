from rest_framework import viewsets
from .models import Child, Teacher, Specialist
from .serializers import ChildSerializer, TeacherSerializer, SpecialistSerializer
from django.shortcuts import render

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer

def adminDashboard(request):
    return render(request, 'admin-dashboard.html')

def assessmentGenerator(request):
    return render(request, 'assessment-generator.html')

def iepGeneration(request):
    return render(request, 'iep-generation.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def parentDashboard(request):
    return render(request, 'parent-dashboard.html')

def parentHomepage(request):
    return render(request, 'parent-homepage.html')

def parentSubmitted(request):
    return render(request, 'parent-submitted.html')

def savedFiles(request):
    return render(request, 'saved-files.html')

def specialistAssessment(request):
    return render(request, 'specialist-assessment.html')

def specialistDashboard(request):
    return render(request, 'specialist-dashboard.html')

def specialistProgress(request):
    return render(request, 'specialist-progress.html')

def studentsEnrolled(request):
    return render(request, 'students-enrolled.html')

def teacherDashboard(request):
    return render(request, 'teacher-dashboard.html')

def weeklyProgress(request):
    return render(request, 'weekly-progress.html')
