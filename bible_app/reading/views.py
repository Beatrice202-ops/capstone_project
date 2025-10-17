from rest_framework import viewsets
from .models import BibleVerse, ReadingProgress, Reminder
from .serializers import BibleVerseSerializer, ReadingProgressSerializer, ReminderSerializer

class BibleVerseViewSet(viewsets.ModelViewSet):
    queryset = BibleVerse.objects.all()
    serializer_class = BibleVerseSerializer

class ReadingProgressViewSet(viewsets.ModelViewSet):
    queryset = ReadingProgress.objects.all()
    serializer_class = ReadingProgressSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
