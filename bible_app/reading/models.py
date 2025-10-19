from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BibleVerse(models.Model):
    book = models.CharField(max_length=100)
    chapter = models.IntegerField()
    verse = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.book} {self.chapter}:{self.verse}"

# Track which verses a user has completed
class ReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True)
    verse = models.ForeignKey(BibleVerse, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.verse} - {self.completed}"

# Store reminder preferences for users
class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reminder_time = models.TimeField()
    message = models.CharField(max_length=255, default="Time to read your Bible! 🙏")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.reminder_time}"
    

