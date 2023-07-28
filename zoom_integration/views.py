from django.shortcuts import render
from rest_framework import viewsets
from .models import ZoomMeeting
from .serializers import ZoomMeetingSerializer

# Create your views here.

class ZoomMeetingViewSet(viewsets.ModelViewSet):
    queryset = ZoomMeeting.objects.all()
    serializer_class = ZoomMeetingSerializer
