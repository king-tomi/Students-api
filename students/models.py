from django.db import models

# Create your models here.
class Level(models.IntegerChoices):
    FIRST = 100, "first"
    SECOND = 200, "second"
    THIRD = 300, "third"
    FOURTH = 400, "fourth"
    FIFTH = 500, "fifth"
    SIXTH = 600, "sixth"
class Student(models.Model):

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(unique=True ,max_length=250, null=True)
    other_names = models.CharField(max_length=250,null=True)
    age = models.IntegerField()
    discipline = models.CharField(max_length=250)
    dob = models.DateField()
    registered = models.DateField(auto_now_add=True)
    level = models.IntegerField(choices=Level.choices)
    matric = models.IntegerField()
    gender = models.CharField(max_length=6)
    cgpa = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=3)
    passport_photo = models.ImageField(upload_to='passports')

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.other_names}"