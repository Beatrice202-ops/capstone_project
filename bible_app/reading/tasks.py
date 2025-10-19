from background_task import background
from django.core.mail import send_mail
from django.utils import timezone
from .models import Reminder

def send_bible_reminders():
    now = timezone.localtime(timezone.now())
    current_time = now.strftime('%H:%M')  # e.g., "07:00"

    reminders = Reminder.objects.filter(is_active=True)
    for reminder in reminders:
        reminder_time = reminder.time.strftime('%H:%M')
        if reminder_time == current_time:
            send_mail(
                subject="Bible Reading Reminder",
                message=reminder.message,
                from_email="uzomabeatrice3@gmail.com,
                recipient_list=[reminder.user.email],
                fail_silently=False,
            )


