from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, GetCSRF, TeacherViewSet, StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teachers',TeacherViewSet)
router.register('students',StudentViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('get_csrf/',GetCSRF.as_view(),name='get-csrf'),
    path('',include(router.urls))
]



# /teachers/: List all teachers and create a new teacher.
# /teachers/{id}/: Retrieve, update, or delete a specific teacher.
# /students/: List all students and create a new student.
# /students/{id}/: Retrieve, update, or delete a specific student.