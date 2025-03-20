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
    UserRegistrationView,
    UserLoginView,
    mood_summary,  
    mindfulness_challenges,  
    helplines,  
    mood_alerts,  
    mindfulness_quotes,  
    mood_feedback,  # New endpoint
    meditation_notifications,  # New endpoint
    peer_connect,  # New endpoint
    resources_podcasts,  # New endpoint
    resources_assessment_tools,  # New endpoint
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
    path('auth/register/', UserRegistrationView.as_view(), name='user_register'),
    path('auth/login/', UserLoginView.as_view(), name='user_login'),
    path('mood/summary/', mood_summary, name='mood_summary'),  # Mood Summary
    path('mindfulness/challenges/', mindfulness_challenges, name='mindfulness_challenges'),  # Mindfulness Challenges
    path('resources/helplines/', helplines, name='helplines'),  # Helplines
    path('mood/alerts/', mood_alerts, name='mood_alerts'),  # Mood Alerts
    path('mindfulness/quotes/', mindfulness_quotes, name='mindfulness_quotes'),  # Mindfulness Quotes
    path('mood/feedback/', mood_feedback, name='mood_feedback'),  # Mood Feedback
    path('meditation/notifications/', meditation_notifications, name='meditation_notifications'),  # Meditation Notifications
    path('support/peer-connect/', peer_connect, name='peer_connect'),  # Peer Connect
    path('resources/podcasts/', resources_podcasts, name='resources_podcasts'),  # Resources Podcasts
    path('resources/assessment-tools/', resources_assessment_tools, name='resources_assessment_tools'),  # Resources Assessment Tools
]