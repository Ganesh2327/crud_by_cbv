from django.db import models
from django.urls import reverse
# Create your models here.


class School(models.Model):
    SchoolName=models.CharField(max_length=100)
    SchoolPrincpal=models.CharField(max_length=100)
    SchoolLocation=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.SchoolName
    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})

class Student(models.Model):
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    SchoolName=models.ForeignKey(School,on_delete=models.CASCADE,related_name='Students')

    def __str__(self) -> str:
        return self.Sname