from rest_framework import serializers
from .models import Student
from .models import Branch

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=50)
    # mobile = serializers.CharField(max_length=12)
    # branch = serializers.CharField(max_length=20)
    
    class Meta:
        model = Student
        fields = ('id', 'name', 'mobile', 'branch_id')
    
    # def create(self, data):
    #     return Student.objects.create(**data)

class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('id', 'name', 'status')
        # fields = '__all__'
        # def create(data):
        #     return Branch.objects.create(**data)

        # def update(data):
        #     return Branch.objects.update(**data)