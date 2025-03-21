from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    mood = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user_id} - {self.mood} on {self.date}"

class MoodAnalytics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    mood = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user_id} - {self.mood} on {self.date}"

class MindfulnessExercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    stress_level = models.CharField(max_length=50)
    is_challenge = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class VideoResource(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Resource(models.Model):
    TYPE_CHOICES = [
        ('helpline', 'Helpline'),
        ('quote', 'Quote'),
        # Add other types as needed
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    content = models.TextField()

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} on {self.created_at}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_time = models.TimeField()  # Store time for notifications
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} at {self.notification_time}"

class PeerConnection(models.Model):
    user = models.ForeignKey(User, related_name='user_connections', on_delete=models.CASCADE)
    peer = models.ForeignKey(User, related_name='peer_connections', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} connected with {self.peer.username}"