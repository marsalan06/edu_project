from django.urls import path, include
from .views import get_expertise_choices, TeacherSessionAPIView,available_teacher




urlpatterns = [
    path('choices/', get_expertise_choices, name='expertise_choices'),
    path('class-sessions/', TeacherSessionAPIView.as_view(), name='class-session-list-create'),
    path('class-sessions/<int:pk>', TeacherSessionAPIView.as_view(), name='class-session-detail'),
    path('available-teachers/', available_teacher, name='available_teacher'),

]