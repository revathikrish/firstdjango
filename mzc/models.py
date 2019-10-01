from django.db import models

# Create your models here.

GENDER_CHOICES=(
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHERS')
)
class Students(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=10)
    address=models.TextField()
    course=models.CharField(max_length=50)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')

class Faculty(models.Model):
    name=models.CharField(max_length=15)
    designation=models.CharField(max_length=15)
    address=models.TextField()
    course=models.CharField(max_length=10)    