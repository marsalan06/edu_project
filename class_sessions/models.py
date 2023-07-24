from django.db import models
import datetime
# Create your models here.
from django.db import models
# from django.contrib.auth.models import User
from users.models import Teacher, Student


class TeachingSession(models.Model):
    topic = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    description = models.TextField()
    expertise = models.CharField(max_length=255,choices=Teacher.EXPERTISE_CHOICES)

    def __str__(self):
        return f"{self.teacher.user.username} -{self.student.user.username} - {self.date} {self.start_time}"
