from django.contrib import admin

from .models import Student
from .models import StudentProfile
from .models import Branch

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile', 'branch_id']

@admin.register(StudentProfile)
class StudentProfile(admin.ModelAdmin):
    list_display = ['id', 'address1', 'address2', 'city', 'state', 'student_id']

@admin.register(Branch)
class Branch(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']