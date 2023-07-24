from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class Teacher(models.Model):

    EXPERTISE_CHOICES = (
    ('phy', 'Physics'),
    ('chem', 'Chemistry'),
    ('math', 'Mathematics'),
    ('comp', 'Computer Science'),
    ('humn', 'Humanities'),
    ('bio', 'Biology'),
    ('zoo', 'Zoology'),
    ('bot', 'Botany'),
)

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='teacher')
    teacher_name = models.CharField(max_length=255,null=True,blank=True)
    qualifications = models.CharField(max_length=255)
    expertise = MultiSelectField(choices=EXPERTISE_CHOICES, max_length=255)

    def __str__(self) -> str:
        return self.teacher_name
    


class Student(models.Model):

    SPECIALIZATION_CHOICES = (
    ('science', 'Science'),
    ('arts', 'Arts'),
    ('commerce', 'Commerce'),
)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    dob = models.DateField()
    specialization = models.CharField(max_length=20, choices=SPECIALIZATION_CHOICES)

    def __str__(self):
        return self.user.username