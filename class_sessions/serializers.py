from rest_framework import serializers
from users.models import Teacher, Student
from .models import TeachingSession
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers



class TeachingSessionSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    # expertise = serializers.ChoiceField(choices=[])
    # expertise = serializers.ListField(child=serializers.CharField())
    expertise = serializers.CharField()

    class Meta:
        model = TeachingSession
        fields = ['id', 'topic','teacher', 'student', 'date', 'start_time', 'description', 'expertise']

    def create(self, validated_data):
        print("====validated data====", validated_data)
        print(validated_data['expertise'])
        print(validated_data['teacher'])
        teacher_user = User.objects.filter(username=validated_data['teacher'])
        print(teacher_user)
        list_expertise = Teacher.objects.filter(teacher_name=validated_data['teacher']).values('expertise')
        print("====kist of experties ====",list_expertise)
        print("=====inside for loop====")
        print(list_expertise[0]['expertise'])
        if validated_data['expertise'] not in list(list_expertise[0]['expertise']):
            print("====if case====")
            validated_data['expertise'] = list(list_expertise[0]['expertise'])[0]
            print(validated_data)
            # teacher_session_object = TeachingSession.objects.create(**validated_data)
            teacher_session_object = TeachingSession.objects.create(**validated_data)
        else:
            print("====else case====")
        print("======i am here-----")
        print(validated_data)
        teacher_session_object = TeachingSession.objects.create(**validated_data)
        return teacher_session_object