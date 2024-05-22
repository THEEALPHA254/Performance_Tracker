from django.urls import path
from . import views

urlpatterns = [
  path('students/', views.StudentView.as_view()),
  path('subjects/', views.SubjectView.as_view()),
  path('results/', views.ResultView.as_view()),
]