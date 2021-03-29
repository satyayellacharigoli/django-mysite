from rest_framework import serializers
from .models import Student
from .models import Branch

class StudentSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.name')
    class Meta:
        model = Student
        fields = ('id', 'name', 'mobile', 'branch_id', 'branch_name')
    
class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('id', 'name', 'status')