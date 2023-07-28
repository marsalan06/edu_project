from django.db import models
from django.contrib.auth.models import User
from class_sessions.models import TeachingSession

# Create your models here.
class ZoomMeeting(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('started', 'Started'),
        ('interrupted', 'Interrupted'),
        ('completed', 'Completed'),
    ]

    teaching_session = models.ForeignKey(TeachingSession, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    meeting_id = models.CharField(max_length=255)
    duration = models.FloatField()
    join_url = models.URLField()

    def __str__(self):
        return f"{self.teaching_session.topic} - {self.status}"
