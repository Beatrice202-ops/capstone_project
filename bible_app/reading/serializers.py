from rest_framework import serializers
from .models import User, BibleVerse, ReadingPlans, reminders 

class Userserializer(serializers.Modelserializer):
    class meta:
        model = User
        field = ['id', 'username', 'email']

class BibleVerseserializer(serializers.Modelserializer):
    class meta:
        model = BibleVerse
        field = {'id', 'books' 'chapter,' 'verses' 'text'}
        
class ReadingPlanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ReadingPlan
        fields = ['id', 'user', 'title', 'start_date', 'end_date', 'completed']

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'user', 'message', 'time', 'is_active']
        