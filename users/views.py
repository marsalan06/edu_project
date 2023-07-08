from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, TeacherSerializer, StudentSerializer
from django.views import View
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework import viewsets
from .models import Teacher, Student





class UserRegistrationView(APIView):
    @csrf_exempt if settings.DEBUG else None
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    @csrf_exempt if settings.DEBUG else None
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # Generate and return a token or session ID for subsequent requests
            return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)


class GetCSRF(View):
    def get(self, request):
        csrf_token = get_token(request)
        return JsonResponse({'csrf':csrf_token})
    
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer