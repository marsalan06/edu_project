# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Teacher

from .models import TeachingSession
from .serializers import TeachingSessionSerializer


def get_expertise_choices(request):
    print("=============testing here====")
    teacher_id = request.GET.get('teacher_id')
    if teacher_id:
        teacher = Teacher.objects.filter(id=teacher_id).first()
        if teacher:
            expertise_choices = teacher.expertise
            return JsonResponse({'choices': list(expertise_choices)})

    return JsonResponse({'choices': []})


class TeacherSessionAPIView(APIView):
    def get(self, request):
        class_sessions = TeachingSession.objects.all()
        serializer = TeachingSessionSerializer(class_sessions, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("======request.data==", request.data)
        serializer = TeachingSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        class_session = self.get_class_session(pk)
        serializer = TeachingSessionSerializer(
            class_session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        class_session = self.get_class_session(pk)
        class_session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_class_session(self, pk):
        try:
            return TeachingSession.objects.get(pk=pk)
        except TeachingSession.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND


def available_teacher(request):
    # Retrieve a list of available teachers from your model (Teacher model)
    # teachers = Teacher.objects.all()  # Replace with your actual query

    context = {}

    if request.user.is_authenticated:
        context['is_authenticated'] = True
        context['username'] = request.user.username
    else:
        context['is_authenticated'] = False

    teachers_list = Teacher.objects.all().values()
    context['teachers'] = teachers_list
    if 'zoom_access_token' in request.session:
        access_token = request.session['zoom_access_token']
        context['access_token'] = access_token
    if 'zoom_access_token_expires_at' in request.session:
        expiry = request.session['zoom_access_token_expires_at']
        context['expiry'] = expiry
    print("=====context====")
    print(context)
    return render(request, 'teacher_availability.html', context)
