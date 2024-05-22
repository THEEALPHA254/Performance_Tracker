from rest_framework import serializers
from .models import Student, Subject, Result

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name']  # Include only id and name fields

class SubjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subject
    fields = ['id', 'name']  # Include only id and name fields

class ResultSerializer(serializers.ModelSerializer):
  class Meta:
    model = Result
    fields = ['id', 'student', 'subject', 'score']