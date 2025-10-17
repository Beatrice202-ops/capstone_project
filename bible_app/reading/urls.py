from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BibleVerseViewSet, ReadingProgressViewSet, ReminderViewSet

router = DefaultRouter()
router.register(r'verses', BibleVerseViewSet)
router.register(r'progress', ReadingProgressViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
