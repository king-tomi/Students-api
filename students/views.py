from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Student
from .serializers import StudentSerializer, StudentSerializerWithCGPA

#all the endpoints
class StudentsAPIView(generics.ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentByIDView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializerWithCGPA

#class StudentByFirstNameView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    lookup_field = "first_name"
    serializer_class = StudentSerializerWithCGPA

class StudentByFirstNameViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    lookup_field = "first_name"
    serializer_class = StudentSerializerWithCGPA

class StudentByLastNameView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    lookup_field = "last_name"
    serializer_class = StudentSerializerWithCGPA

class StudentsByLevelView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    lookup_field = "level"
    serializer_class = StudentSerializerWithCGPA

class StudentsByGenderView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    lookup_field = "gender"
    serializer_class = StudentSerializer

class StudentsByAgeView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    lookup_field = "age"
    serializer_class = StudentSerializer