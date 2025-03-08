from django.db import models

class MoodEntry(models.Model):
    user_id = models.IntegerField()  # In a real app, use a User model
    mood = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user_id} - {self.mood} on {self.date}"
class MoodAnalytics(models.Model):
    user_id = models.IntegerField()  # In a real app, use a User model
    mood = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user_id} - {self.mood} on {self.date}"

class MindfulnessExercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    stress_level = models.CharField(max_length=50)

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