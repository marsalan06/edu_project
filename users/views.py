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
from django.contrib.auth.models import User

def index(request):
    return render(request,'index.html')

class UserRegistrationView(APIView):
    @csrf_exempt if settings.DEBUG else None
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        context = {}
        return render(request, 'Signup.html',context)

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
    
    def get(self,request):
        context = {}
        return render(request, 'Login.html',context)


class GetCSRF(View):
    def get(self, request):
        csrf_token = get_token(request)
        return JsonResponse({'csrf':csrf_token})
    
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def create(self, request, *args, **kwargs):
        # Check if the user already exists
        username = request.data.get('user')['username']
        print("=========12121=====")
        print(username)
        try:
            print("======try=====")
            user = User.objects.get(username=username)
            print(user)
            if Teacher.objects.filter(user=user.id).exists():
                print("====teacher exists====")
                return Response({"message": "User already has a teacher record."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            print("=====user doesnt exists=====")
            # Create the user
            user_serializer = UserSerializer(data=request.data.get('user'))
            if user_serializer.is_valid():
                user = user_serializer.save()
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Check if the teacher record already exists
        # Create the teacher
        print("=========teacher level=======")
        request.data['user'] = user.id
        print(request.data)
        teacher_serializer = TeacherSerializer(data=request.data)
        if teacher_serializer.is_valid():
            teacher_serializer.save(user=user)
        else:
            return Response(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(teacher_serializer.data, status=status.HTTP_201_CREATED)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        # Check if the user already exists
        username = request.data.get('user')['username']
        print("=========12121=====")
        print(username)
        try:
            print("======try=====")
            user = User.objects.get(username=username)
            print(user)
            if Student.objects.filter(user=user.id).exists():
                print("====student exists====")
                return Response({"message": "User already has a student record."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            print("=====user doesnt exists=====")
            # Create the user
            user_serializer = UserSerializer(data=request.data.get('user'))
            if user_serializer.is_valid():
                user = user_serializer.save()
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Check if the student record already exists
        # Create the student
        print("=========student level=======")
        request.data['user'] = user.id
        print(request.data)
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save(user=user)
        else:
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(student_serializer.data, status=status.HTTP_201_CREATED)