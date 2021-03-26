from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Student
from .models import Branch
from student.serializers import StudentSerializer
from student.serializers import BranchSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
import io

from django.views.decorators.csrf import csrf_exempt, csrf_protect


from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


def get_all_students(request):
    if request.method == 'GET':
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

@csrf_exempt
def student_create(request):
    json_data = request.body
    stream = io.BytesIO(json_data)
    req_data = JSONParser().parse(stream)
    serilizer = StudentSerilizer(data = req_data)
    if serilizer.is_valid():
        serilizer.save()
        return HttpResponse('New Student Added.')
    return HttpResponse('Please check your data.')


class BranchViewSets(viewsets.ModelViewSet):
    # queryset = Branch.objects.all()
    # serilizer_class = BranchSerializer
    def list(request):
        queryset = Branch.objects.all()
        serializer = BranchSerializer(queryset, many=True)
        data = JSONRenderer().render(serializer.data)
        return HttpResponse(data, content_type='application/json')
    
    @csrf_exempt
    def create(request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        req_data = JSONParser().parse(stream)
        serilizer = BranchSerializer(data = req_data)
        if serilizer.is_valid():
            serilizer.save()
            return HttpResponse('New Branch added.')
        return HttpResponse('Please check your data.')

    def retrieve(request, pk=None):
        try:
            queryset = Branch.objects.get(id = pk)
            serializer = BranchSerializer(queryset)
            result = JSONRenderer().render(serializer.data)
            return HttpResponse(result, content_type='applciation.json')
        except Branch.DoesNotExist:
            return HttpResponse("No data found.")

    # @csrf_exempt
    # def update(request, pk=None):
    #     try:
    #         queryset =  Branch.objects.get(id=pk)
    #         json_data = request.body
    #         stream = io.BytesIO(json_data)
    #         req_data = JSONParser().parse(stream)
    #         serializer = BranchSerializer(queryset,data=request)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return HttpResponse('Branch updated successfully.')
    #         else:
    #             return HttpResponse('failed.')
    #     except Branch.DoesNotExist:
    #         return HttpResponse("No data found.")

    @csrf_exempt
    def destroy(request, pk=None):
        try:
            queryset = Branch.objects.get(id=pk)
            queryset.delete()
            return HttpResponse('Branch deleted.')
        except Branch.DoesNotExist:
            return HttpResponse('No data found')