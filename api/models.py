from django.db import models

class MoodEntry(models.Model):
    user_id = models.IntegerField()  # You might want to use a User model instead
    mood = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

class Meditation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()

class Resource(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    resource_type = models.CharField(max_length=100)  # e.g., article, video, podcast