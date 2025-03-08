from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MoodEntry, MoodAnalytics, MindfulnessExercise, FAQ, VideoResource
from .serializers import MoodEntrySerializer, MoodAnalyticsSerializer, MindfulnessExerciseSerializer, FAQSerializer, VideoResourceSerializer

# 1. Retrieve a list of guided meditations based on user preferences
@api_view(['GET'])
def get_meditations(request):
    # Placeholder for meditation data
    meditations = [
        {"id": 1, "title": "Stress Relief Meditation", "duration": "10 min"},
        {"id": 2, "title": "Focus Meditation", "duration": "15 min"},
    ]
    return Response(meditations)

# 2. Log and analyze mood entries over time
class MoodEntryListCreate(generics.ListCreateAPIView):
    queryset = MoodEntry.objects.all()
    serializer_class = MoodEntrySerializer

# 3. Access educational articles on mental health topics
@api_view(['GET'])
def get_articles(request):
    # Placeholder for articles
    articles = [
        {"id": 1, "title": "Understanding Anxiety", "url": "https://example.com/anxiety"},
        {"id": 2, "title": "Coping with Depression", "url": "https://example.com/depression"},
    ]
    return Response(articles)

# 4. Connect users with community support groups
@api_view(['GET'])
def get_community_support(request):
    # Placeholder for community support groups
    support_groups = [
        {"id": 1, "name": "Anxiety Support Group", "platform": "Discord"},
        {"id": 2, "name": "Depression Support Group", "platform": "Reddit"},
    ]
    return Response(support_groups)

# 5. Provide daily wellness tips tailored to user preferences and mood
@api_view(['GET'])
def get_wellness_tips(request):
    # Placeholder for wellness tips
    tips = [
        {"id": 1, "tip": "Take a 5-minute break to breathe deeply."},
        {"id": 2, "tip": "Write down three things you are grateful for."},
    ]
    return Response(tips)

# 6. Mood Analytics
@api_view(['GET', 'POST'])
def mood_analytics_list(request):
    if request.method == 'GET':
        analytics = MoodAnalytics.objects.all()
        serializer = MoodAnalyticsSerializer(analytics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MoodAnalyticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# 7. Mindfulness Exercises
@api_view(['GET', 'POST'])
def mindfulness_exercise_list(request):
    if request.method == 'GET':
        exercises = MindfulnessExercise.objects.all()
        serializer = MindfulnessExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MindfulnessExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# 8. Mental Health FAQ
@api_view(['GET'])
def faq_list(request):
    faqs = FAQ.objects.all()
    serializer = FAQSerializer(faqs, many=True)
    return Response(serializer.data)

# 9. Weather Mood Insights (Placeholder)
@api_view(['GET'])
def weather_mood_insights(request):
    # Placeholder logic for weather mood insights
    insights = {
        "sunny": "You might feel more energetic and positive.",
        "rainy": "You might feel more reflective or calm."
    }
    return Response(insights)

# 10. Video Resources
@api_view(['GET'])
def video_resource_list(request):
    videos = VideoResource.objects.all()
    serializer = VideoResourceSerializer(videos, many=True)
    return Response(serializer.data)