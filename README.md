# mental-wellness-companion
This document provides detailed information about each endpoint in the Mindfulness and Mood Tracking API. Each section includes the HTTP method, URL, headers, and example request/response bodies.

---

## 1. User Registration

- **Method**: POST
- **URL**: `http://127.0.0.1:8000/auth/register/`
- **Body** (JSON):
  ```json
  {
      "username": "testuser",
      "password": "testpassword"
  }

## 2. User Login
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/auth/login/`
- **Body** (JSON):
 ```json
{
    "username": "testuser",
    "password": "testpassword"
}
```
## 3. Get Guided Meditations
- **Method**: GET
- **URL**: http://127.0.0.1:8000/mindfulness/meditations/
Response:
```json
[
    {"id": 1, "title": "Stress Relief Meditation", "duration": "10 min"},
    {"id": 2, "title": "Focus Meditation", "duration": "15 min"}
]
```
## 4. Log Mood Entry
- **Method**: POST
- **URL**: http://127.0.0.1:8000/mood/track/
Headers:
Authorization: Token <your_token_here>
Body (JSON):
```json
{
    "mood": "happy",
    "notes": "Had a great day!"
}
```
## 5. Get Mood Analytics
- **Method**: GET
- **URL**: http://127.0.0.1:8000/mood/analytics/
Headers:
Authorization: Token <your_token_here>

## 6. Get Articles on Mental Health
- **Method**: GET
- **URL**: http://127.0.0.1:8000/resources/articles/
Response:
```json
[
    {"id": 1, "title": "Understanding Anxiety", "url": "https://example.com/anxiety"},
    {"id": 2, "title": "Coping with Depression", "url": "https://example.com/depression"}
]
```
## 7. Get Community Support Groups
- **Method**: GET
- **URL**: http://127.0.0.1:8000/support/community/
Response:
```json
[
    {"id": 1, "name": "Anxiety Support Group", "platform": "Discord"},
    {"id": 2, "name": "Depression Support Group", "platform": "Reddit"}
]
```
## 8. Get Daily Wellness Tips
- **Method**: GET
- **URL**: http://127.0.0.1:8000/wellness/tips/
Response:
```json
[
    {"id": 1, "tip": "Take a 5-minute break to breathe deeply."},
    {"id": 2, "tip": "Write down three things you are grateful for."}
]
```
## 9. Get Mood Summary
- **Method**: GET
- **URL**: http://127.0.0.1:8000/mood/summary/
Headers:
Authorization: Token <your_token_here>

## 10. Get Mood Alerts
- **Method**: GET
- **URL**: http://127.0.0.1:8000/mood/alerts/
Headers:
Authorization: Token <your_token_here>

## 11. Get Mental Health FAQs
- **Method**: GET
- **URL**: http://127.0.0.1:8000/mental-health/faq/
Response:
```json
[
    {"question": "What is anxiety?", "answer": "Anxiety is..."},
    {"question": "How to cope with stress?", "answer": "You can cope by..."}
]
```
## 12. Get Weather Mood Insights
- **Method**: GET
- **URL**: http://127.0.0.1:8000/weather/mood-insights/
Response:
```json
{
    "sunny": "You might feel more energetic and positive.",
    "rainy": "You might feel more reflective or calm."
}
```
## 13. Get Video Resources
- **Method**: GET
- **URL**: http://127.0.0.1:8000/resources/videos/
Response:
```json
[
    {"id": 1, "title": "Mindfulness Video", "url": "https://example.com/video1"},
    {"id": 2, "title": "Meditation Video", "url": "https://example.com/video2"}
]
```
## 14. Get Mindfulness Challenges
- **Method**: GET
- **URL**: http://127.0.0.1:8000/mindfulness/challenges/
Response:
```json
[
    {"id": 1, "title": "30-Day Mindfulness Challenge", "description": "A challenge to practice mindfulness daily."}
]
```
## 15. Get Mindfulness Quotes
- **Method**: GET
- **URL**: http://127.0.0.1:8000/mindfulness/quotes/
Response:
```json
[
    {"id": 1, "content": "The mind is everything. What you think you become."},
    {"id": 2, "content": "Peace comes from within. Do not seek it without."}
]
```
## 16. Submit Mood Feedback
- **Method**: POST
- **URL**: http://127.0.0.1:8000/mood/feedback/
Headers:
Authorization: Token <your_token_here>
Body (JSON):
```json
{
    "feedback": "This app is really helpful!"
}
```
## 17. Set Meditation Notifications
- **Method**: POST
- **URL**: http://127.0.0.1:8000/meditation/notifications/
Headers:
Authorization: Token <your_token_here>
Body (JSON):
```json
{
    "notification_time": "08:00"
}
```
## 18. Connect with Peers
- **Method**: POST
- **URL**: http://127.0.0.1:8000/support/peer-connect/
Headers:
Authorization: Token <your_token_here>
Body (JSON):
```json
{
    "peer_id": 2  // Replace with the actual user ID you want to connect with
}
```
## 19. Get Resources: Podcasts
- **Method**: GET
- **URL**: http://127.0.0.1:8000/resources/podcasts/
Response:
```json
[
    {"id": 1, "title": "Mental Health Podcast", "url": "https://example.com/podcast1"},
    {"id": 2, "title": "Mindfulness Podcast", "url": "https://example.com/podcast2"}
]
```
## 20. Get Resources: Assessment Tools
- **Method**: GET
- **URL**: http://127.0.0.1:8000/resources/assessment-tools/
Response:
```json
[
    {"id": 1, "title": "Anxiety Assessment", "url": "https://example.com/anxiety-assessment"},
    {"id": 2, "title": "Depression Assessment", "url": "https://example.com/depression-assessment"}
]
