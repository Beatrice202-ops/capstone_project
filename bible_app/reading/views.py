#from django.shortcuts import render
from rest_framework import viewsets
from .models import BibleVerse, ReadingPlan, reminders
from .serializers import BibleVerseserializer, ReadingPlanSerializer, ReminderSerializer

# Create your views here. 
class BibleVerseviewsets(viewsets.ModelViewsets):
    queryset = BibleVerse.objects.all()
    serializer_class = BibleVerseSerializer

class ReadingPlanViewSet(viewsets.ModelViewSet):
    queryset = ReadingPlan.objects.all()
    serializer_class = ReadingPlanSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
