from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Teacher, Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

class TeacherSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    expertise = serializers.ListField()


    class Meta:
        model = Teacher
        fields = ['user', 'qualifications', 'expertise','teacher_name']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print(user_data)
        # user = UserSerializer().create(user_data)
        teacher = Teacher.objects.create(user=user_data, **validated_data)
        return teacher
    
class StudentSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # specialization = serializers.ListField()
    

    class Meta:
        model = Student
        fields = ['user', 'grade', 'dob', 'specialization']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        # user = UserSerializer().create(user_data)
        student = Student.objects.create(user=user_data, **validated_data)
        return student