from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Student
from .models import Branch
from student.serializers import StudentSerializer
from student.serializers import BranchSerializer
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
import io
from django.views.decorators.csrf import csrf_exempt, csrf_protect


from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

def get_all_students(request):
    if request.method == 'GET':
        # queryset = Student.objects.using('dbname').all()
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        data = JSONRenderer().render(serializer.data)
        return HttpResponse(data, content_type='application/json')

def get_student(request, pk):
    if request.method == 'GET':
        if id is not None:
            res_data = Student.objects.get(id=pk)
            serializer = StudentSerializer(res_data)
            data = JSONRenderer().render(serializer.data)
            return HttpResponse(data, content_type='application/json')

# @csrf_exempt
# def student_create(request):
#     json_data = request.body
#     stream = io.BytesIO(json_data)
#     req_data = JSONParser().parse(stream)
#     serilizer = StudentSerilizer(data = req_data)
#     if serilizer.is_valid():
#         serilizer.save()
#         return HttpResponse('New Student Added.')
#     return HttpResponse('Please check your data.')


class BranchViewSets(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
