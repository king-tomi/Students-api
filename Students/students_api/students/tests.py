from django.test import TestCase

# Create your tests here.
from .models import Student

from datetime import date, datetime
from decimal import Decimal

class StudentTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        return Student.objects.create(first_name="Tomisin", last_name = "Ayodabo", other_names = "Kolawole", age = 21, dob = date(2000,3,31), level = 300, registered = datetime.now(), matric = 207195, gender = 'male', cgpa = 3.45, passport_photo="./passports/Snapchat-2042115295.jpg", discipline = "Computer Science")

    def test_first_name(self):
        student = Student.objects.get(first_name="Tomisin")
        self.assertEquals(student.first_name, "Tomisin")

    def test_cgpa(self):
        student = Student.objects.get(first_name="Tomisin")
        self.assertEquals(student.cgpa, Decimal('3.45'))

    def test_discipline(self):
        student = Student.objects.get(first_name="Tomisin")
        self.assertEquals(student.discipline, "Computer Science")

    def test_age(self):
        student = Student.objects.get(first_name="Tomisin")
        self.assertEquals(student.age, 21)