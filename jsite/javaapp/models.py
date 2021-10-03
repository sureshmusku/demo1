from django.db import models

# Create your models here.
class Student(models.Model):
    def __str__(self):
        return "Name"+self.name+" Marks"+str(self.marks)
    name=models.CharField(max_length=100)
    marks=models.IntegerField()
