from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import serializers
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import MoodEntry, MoodAnalytics, MindfulnessExercise, FAQ, VideoResource, Resource
from .serializers import (
    MoodEntrySerializer,
    MoodAnalyticsSerializer,
    MindfulnessExerciseSerializer,
    FAQSerializer,
    VideoResourceSerializer,
    ResourceSerializer,  # Assuming you have a ResourceSerializer for helplines and quotes
)

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

# User Registration View
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# User Login View
class UserLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User  does not exist'}, status=status.HTTP_400_BAD_REQUEST)

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
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

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

# 11. Mood Summary
@api_view(['GET'])
def mood_summary(request):
    if request.method == 'GET':
        user = request.user
        mood_entries = MoodEntry.objects.filter(user=user)
        serializer = MoodEntrySerializer(mood_entries, many=True)
        return Response(serializer.data)

# 12. Mindfulness Challenges
@api_view(['GET'])
def mindfulness_challenges(request):
    challenges = MindfulnessExercise.objects.filter(is_challenge=True)  # Ensure this field exists
    serializer = MindfulnessExerciseSerializer(challenges, many=True)
    return Response(serializer.data)

#13. Helplines
@api_view(['GET'])
def helplines(request):
    if request.method == 'GET':
        helplines = Resource.objects.filter(type='helpline')
        serializer = ResourceSerializer(helplines, many=True)
        return Response(serializer.data)

# 14. Mood Alerts
@api_view(['GET'])
def mood_alerts(request):
    if request.method == 'GET':
        user = request.user
        mood_entries = MoodEntry.objects.filter(user=user, mood__in=['sad', 'anxious'])
        serializer = MoodEntrySerializer(mood_entries, many=True)
        return Response(serializer.data)

# 15. Mindfulness Quotes
@api_view(['GET'])
def mindfulness_quotes(request):
    if request.method == 'GET':
        quotes = Resource.objects.filter(type='quote')
        serializer = ResourceSerializer(quotes, many=True)
        return Response(serializer.data)

#16. Mood Feedback
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mood_feedback(request):
    feedback = request.data.get('feedback')
    user = request.user

    # Save feedback logic (you may want to create a Feedback model)
    # For now, we'll just return a success message
    return Response({'message': 'Feedback received successfully!'}, status=status.HTTP_201_CREATED)

#17. Meditation Notifications
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def meditation_notifications(request):
    notification_time = request.data.get('notification_time')
    user = request.user

    # Logic to save notification time (you may want to create a Notification model)
    # For now, we'll just return a success message
    return Response({'message': 'Notification set successfully!'}, status=status.HTTP_201_CREATED)

#18. Peer Connect
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def peer_connect(request):
    peer_id = request.data.get('peer_id')  # ID of the user to connect with
    user = request.user

    # Logic to connect users (you may want to create a PeerConnection model)
    # For now, we'll just return a success message
    return Response({'message': f'Connected with user {peer_id} successfully!'}, status=status.HTTP_201_CREATED)

#19. Resources: Podcasts
@api_view(['GET'])
def resources_podcasts(request):
    # Placeholder for podcast data
    podcasts = [
        {"id": 1, "title": "Mental Health Podcast", "url": "https://example.com/podcast1"},
        {"id": 2, "title": "Mindfulness Podcast", "url": "https://example.com/podcast2"},
    ]
    return Response(podcasts)

#20. Resources: Assessment Tools
@api_view(['GET'])
def resources_assessment_tools(request):
    # Placeholder for assessment tools
    assessment_tools = [
        {"id": 1, "title": "Anxiety Assessment", "url": "https://example.com/anxiety-assessment"},
        {"id": 2, "title": "Depression Assessment", "url": "https://example.com/depression-assessment"},
    ]
    return Response(assessment_tools)