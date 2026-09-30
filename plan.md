# Meditation Mindings – Python-Based REST API Project

## Project Overview
**Meditation Mindings** is a backend API service developed using Python and Django to manage meditation sessions, user progress, and daily habit tracking. It provides a RESTful interface for client applications to interact with the system.

## Features
- **User Management**: Registration and management of user accounts.
- **Meditation Sessions**: CRUD operations for meditation sessions (guided/unguided).
- **Activity Logging**: Track user progress by logging completed sessions with notes.
- **Data Persistence**: Uses SQLite for lightweight and efficient data storage.
- **Validation**: Robust input validation (e.g., ensuring positive session durations).
- **Error Handling**: Structured JSON error responses for better client debugging.

## Technology Stack
- **Language**: Python 3
- **Framework**: Django 5.2.8 & Django REST Framework 3.16.1
- **Database**: SQLite
- **Testing**: Django Test Framework (Automated), Postman (Manual)

## Project Structure
```
MeditationMindings/
├── manage.py                # Django command-line utility
├── db.sqlite3               # SQLite database file
├── meditation_project/      # Project configuration
│   ├── settings.py          # App settings (Installed apps, DB, etc.)
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI entry point
└── api/                     # Main application logic
    ├── models.py            # Database models (User, MeditationSession, ActivityLog)
    ├── serializers.py       # JSON serializers for models
    ├── views.py             # API ViewSets (Business logic)
    ├── urls.py              # App-specific URL routing
    └── tests.py             # Automated tests
```

## Setup Instructions

### Prerequisites
- Python 3.x installed
- `pip` (Python package manager)

### Installation
1. **Clone/Navigate to the directory**:
   ```bash
   cd /home/bluerabbit/Desktop/MeditationMindings
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django djangorestframework
   ```

4. **Apply Migrations**:
   ```bash
   python3 manage.py migrate
   ```

5. **Run the Server**:
   ```bash
   python3 manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/api/`.

## API Endpoints

### Users
- **List Users**: `GET /api/users/`
- **Create User**: `POST /api/users/`
  - Body: `{"username": "...", "password": "...", "email": "..."}`

### Meditation Sessions
- **List Sessions**: `GET /api/sessions/`
- **Create Session**: `POST /api/sessions/`
  - Body: `{"title": "...", "description": "...", "duration_minutes": 10}`
- **Retrieve Session**: `GET /api/sessions/<id>/`
- **Update Session**: `PUT /api/sessions/<id>/`
- **Delete Session**: `DELETE /api/sessions/<id>/`

### Activity Logs
- **List Logs**: `GET /api/activity-logs/`
- **Create Log**: `POST /api/activity-logs/`
  - Body: `{"user": <user_id>, "session": <session_id>, "notes": "..."}`

## Testing

### Automated Tests
Run the built-in test suite to verify all endpoints:
```bash
python3 manage.py test api
```
**Coverage**:
- User creation
- Session creation
- Activity logging
- Validation (e.g., negative duration check)

### Manual Testing (Postman)
A Postman collection file `MeditationMindings.postman_collection.json` is included in the project root. Import it into Postman to test the API manually.

## Status
- [x] **Project Initialization**: Django project and app created.
- [x] **Database Design**: Models for User, Session, and Log defined.
- [x] **API Implementation**: Serializers, Views, and URLs configured.
- [x] **Verification**: Automated tests passed.
- [x] **Documentation**: Postman collection and this plan created.