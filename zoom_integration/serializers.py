# serializers.py

from rest_framework import serializers
from .models import ZoomMeeting

class ZoomMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoomMeeting
        fields = '__all__'
