from django.contrib.auth.models import User
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
    user = serializers.StringRelatedField(read_only=True)  # shows username in response
    verse = BibleVerseSerializer(read_only=True)
    verse_id = serializers.PrimaryKeyRelatedField(
    queryset=BibleVerse.objects.all(), source='verse', write_only=True
    )
    class Meta:
        model = ReadingProgress
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

