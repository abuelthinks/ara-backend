from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ChildViewSet, 
    TeacherViewSet, 
    SpecialistViewSet, 
    index,
    adminDashboard,
    assessmentGenerator,
    iepGeneration,
    login,
    parentDashboard,
    parentHomepage,
    parentSubmitted,
    savedFiles,
    specialistAssessment,
    specialistDashboard,
    specialistProgress,
    studentsEnrolled,
    teacherDashboard,
    weeklyProgress,
)

router = DefaultRouter()
router.register(r'children', ChildViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'specialists', SpecialistViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('admin-dashboard/', adminDashboard, name='adminDashboard'),
    path('assessment-generator/', assessmentGenerator, name='assessmentGenerator'),
    path('iep-generation/', iepGeneration, name='iepGeneration'),
    path('login/', login, name='login'),
    path('parent-dashboard/', parentDashboard, name='parentDashboard'),
    path('parent-homepage/', parentHomepage, name='parentHomepage'),
    path('parent-submitted/', parentSubmitted, name='parentSubmitted'),
    path('saved-files/', savedFiles, name='savedFiles'),
    path('specialist-assessment/', specialistAssessment, name='specialistAssessment'),
    path('specialist-dashboard/', specialistDashboard, name='specialistDashboard'),
    path('specialist-progress/', specialistProgress, name='specialistProgress'),
    path('students-enrolled/', studentsEnrolled, name='studentsEnrolled'),
    path('teacher-dashboard/', teacherDashboard, name='teacherDashboard'),
    path('weekly-progress/', weeklyProgress, name='weeklyProgress'),
    path('api/', include(router.urls)),
]
