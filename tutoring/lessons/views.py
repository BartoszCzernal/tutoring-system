from django.shortcuts import render
from rest_framework import generics
from .models import Lesson
from .serializers import LessonSerializer


class LessonList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all().order_by('start_date')
    serializer_class = LessonSerializer


class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all().order_by('start_date')
    serializer_class = LessonSerializer
