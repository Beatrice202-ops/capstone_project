from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BibleVerseViewSet, ReadingProgressViewSet, ReminderViewSet, RegisterView

router = DefaultRouter()
router.register(r'verses', BibleVerseViewSet)
router.register(r'progress', ReadingProgressViewSet, basename='progress')
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]
