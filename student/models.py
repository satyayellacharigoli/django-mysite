from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

class Student(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    # datae_of_joining = models.DateField(timezone.now())
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

class StudentProfile(models.Model):
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
