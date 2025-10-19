from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import BibleVerse, ReadingProgress, Reminder
from .serializers import BibleVerseSerializer, ReadingProgressSerializer, ReminderSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .tasks import send_bible_reminders_task

class BibleVerseViewSet(viewsets.ModelViewSet):
    queryset = BibleVerse.objects.all()
    serializer_class = BibleVerseSerializer
    permission_classes = [AllowAny]

class ReadingProgressViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = ReadingProgressSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # return only the logged-in user's progress records
        return ReadingProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # save the user automatically — do NOT expect client to supply it
        serializer.save(user=self.request.user)

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    
    def perform_create(self, serializer):
            reminder = serializer.save(user=self.request.user)
            send_bible_reminders_task(repeat=60)  # check every 60 seconds

    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
