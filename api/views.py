from rest_framework import generics
from .models import MoodEntry, Meditation, Resource
from .serializers import MoodEntrySerializer, MeditationSerializer, ResourceSerializer

class MoodEntryListCreate(generics.ListCreateAPIView):
    queryset = MoodEntry.objects.all()
    serializer_class = MoodEntrySerializer

class MeditationList(generics.ListAPIView):
    queryset = Meditation.objects.all()
    serializer_class = MeditationSerializer

class ResourceList(generics.ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer