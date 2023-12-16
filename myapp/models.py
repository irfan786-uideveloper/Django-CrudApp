from django.db import models

# Create your models here.

class Student(models.Model):

    name=models.CharField(max_length=150)

    course=models.CharField(max_length=100)

    city=models.CharField(max_length=120)

    class Meta:

        db_table='Student_data'