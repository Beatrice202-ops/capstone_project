from rest_framework import serializers
from .models import User, BibleVerse, ReadingProgress, Reminder

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BibleVerseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BibleVerse
        fields = ['id', 'book', 'chapter', 'verse', 'text']

class ReadingProgressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ReadingProgress
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'


