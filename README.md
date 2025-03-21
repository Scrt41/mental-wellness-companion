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
