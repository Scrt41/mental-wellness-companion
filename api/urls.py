from django.urls import path
from .views import MoodEntryListCreate, MeditationList, ResourceList

urlpatterns = [
    path('mood/track/', MoodEntryListCreate.as_view(), name='mood-track'),
    path('mindfulness/meditations/', MeditationList.as_view(), name='meditations'),
    path('resources/articles/', ResourceList.as_view(), name='resources'),
    # Add more endpoints as needed
]