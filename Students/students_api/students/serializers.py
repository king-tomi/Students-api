from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id','first_name','last_name','other_names','age','gender','dob','level','matric','discipline',)


class StudentSerializerWithCGPA(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id','first_name','last_name','other_names','age','gender','dob','level','matric','discipline','cgpa')