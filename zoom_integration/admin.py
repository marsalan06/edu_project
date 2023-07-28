from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import ZoomMeeting

@admin.register(ZoomMeeting)
class ZoomMeetingAdmin(admin.ModelAdmin):
    list_display = ('teaching_session', 'status', 'meeting_id', 'duration', 'join_url')
