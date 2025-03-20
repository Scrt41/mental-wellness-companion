from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MoodEntry, MoodAnalytics, MindfulnessExercise, FAQ, VideoResource, Resource

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

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

# New Resource Serializer
class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'