from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=255)

class Subject(models.Model):
  name = models.CharField(max_length=255)

class Result(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  score = models.IntegerField()