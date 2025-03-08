from django.urls import path
from .views import (
    get_meditations,
    get_articles,
    get_community_support,
    get_wellness_tips,
    MoodEntryListCreate,
    mood_analytics_list,
    mindfulness_exercise_list,
    faq_list,
    weather_mood_insights,
    video_resource_list,
)

urlpatterns = [
    path('mindfulness/meditations/', get_meditations, name='get_meditations'),
    path('mood/track/', MoodEntryListCreate.as_view(), name='mood_entry_list_create'),
    path('resources/articles/', get_articles, name='get_articles'),
    path('support/community/', get_community_support, name='get_community_support'),
    path('wellness/tips/', get_wellness_tips, name='get_wellness_tips'),
    path('mood/analytics/', mood_analytics_list, name='mood_analytics'),
    path('mindfulness/exercises/', mindfulness_exercise_list, name='mindfulness_exercises'),
    path('mental-health/faq/', faq_list, name='mental_health_faq'),
    path('weather/mood-insights/', weather_mood_insights, name='weather_mood_insights'),
    path('resources/videos/', video_resource_list, name='video_resources'),
]