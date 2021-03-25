from django.db import models

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

class Student(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

class StudentProfile(models.Model):
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
