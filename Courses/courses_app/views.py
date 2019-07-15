from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class BranchesView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_course(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single course
    if request.method == 'GET':
        return Response({})
    # delete a single course
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single course
    elif request.method == 'PUT':
        return Response({})
@api_view(['GET', 'POST'])
def get_post_course(request):
    # get all courses
    if request.method == 'GET':
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    # insert a new course
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'category': request.data.get('category'),
            'discription': request.data.get('discription'),
            'logo': request.data.get('logo')
        }
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)