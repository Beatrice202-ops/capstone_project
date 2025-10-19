from background_task import background
from django.core.mail import send_mail
from django.utils import timezone
from .models import Reminder


@background(schedule=60)
def send_bible_reminders_task():
    """
    This task checks for active reminders matching the current time
    and sends reminder emails to users.
    """
    now = timezone.localtime(timezone.now())
    current_time = now.strftime('%H:%M')

    reminders = Reminder.objects.filter(is_active=True)
    for reminder in reminders:
        if reminder.time.strftime('%H:%M') == current_time:
            send_mail(
                subject="Bible Reading Reminder",
                message=reminder.message,
                from_email="uzomabeatrice3@gmail.com",
                recipient_list=[reminder.user.email],
                fail_silently=False,
            )

