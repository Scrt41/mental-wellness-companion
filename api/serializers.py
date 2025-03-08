from rest_framework import serializers
from .models import MoodEntry
from .models import MoodAnalytics, MindfulnessExercise, FAQ, VideoResource

class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = '__all__'

class MoodAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodAnalytics
        fields = '__all__'

class MindfulnessExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MindfulnessExercise
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class VideoResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoResource
        fields = '__all__'