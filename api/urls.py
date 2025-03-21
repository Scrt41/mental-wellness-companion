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
    mood_feedback,  
    meditation_notifications,  
    peer_connect, 
    resources_podcasts,  
    resources_assessment_tools,  
)

urlpatterns = [
    # Mindfulness
    path('mindfulness/meditations/', get_meditations, name='get_meditations'),
    path('mindfulness/exercises/', mindfulness_exercise_list, name='mindfulness_exercises'),
    path('mindfulness/challenges/', mindfulness_challenges, name='mindfulness_challenges'),  
    path('mindfulness/quotes/', mindfulness_quotes, name='mindfulness_quotes'),  
    # Mood
    path('mood/track/', MoodEntryListCreate.as_view(), name='mood_entry_list_create'),
    path('mood/analytics/', mood_analytics_list, name='mood_analytics'),
    path('mood/summary/', mood_summary, name='mood_summary'),  
    path('mood/alerts/', mood_alerts, name='mood_alerts'),  
    path('mood/feedback/', mood_feedback, name='mood_feedback'),  

    # Resources
    path('resources/articles/', get_articles, name='get_articles'),
    path('resources/videos/', video_resource_list, name='video_resources'),
    path('resources/podcasts/', resources_podcasts, name='resources_podcasts'),  
    path('resources/helplines/', helplines, name='helplines'),  
    path('resources/assessment-tools/', resources_assessment_tools, name='resources_assessment_tools'),  

    # Support
    path('support/community/', get_community_support, name='get_community_support'),
    path('support/peer-connect/', peer_connect, name='peer_connect'),  

    # Wellness
    path('wellness/tips/', get_wellness_tips, name='get_wellness_tips'),

    # Mental Health
    path('mental-health/faq/', faq_list, name='mental_health_faq'),

    # Weather
    path('weather/mood-insights/', weather_mood_insights, name='weather_mood_insights'),

    # Authentication
    path('auth/register/', UserRegistrationView.as_view(), name='user_register'),
    path('auth/login/', UserLoginView.as_view(), name='user_login'),

    # Meditation
    path('meditation/notifications/', meditation_notifications, name='meditation_notifications'),  
]