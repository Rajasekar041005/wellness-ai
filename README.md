# Health Assistant Chatbot - Django Project

A simple Django-based health assistant chatbot with login functionality.

## Features
- Login page with Bootstrap 5 UI
- Health assistant chatbot with colorful interface
- Disease information database (cancer, diabetes, fever, headache, hypertension, asthma, arthritis, cold)
- Provides explanations, solutions, food recommendations, and exercise advice

## Credentials
- **User ID**: 1234
- **Password**: gym

## Setup Instructions

### 1. Create Virtual Environment
```powershell
python -m venv venv
```

### 2. Activate Virtual Environment
```powershell
venv\Scripts\activate
```

### 3. Install Django
```powershell
pip install django
```
or
```powershell
pip install -r requirements.txt
```

### 4. Run Migrations
```powershell
python manage.py migrate
```

### 5. Start Development Server
```powershell
python manage.py runserver
```

### 6. Access the Application
Open your browser and navigate to:
- **Login Page**: http://127.0.0.1:8000/
- After login, you'll be redirected to the chatbot page

## Project Structure
```
health care/
├── healthassistant/          # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── chatapp/                  # Main application
│   ├── __init__.py
│   ├── views.py             # Login and chatbot views
│   ├── urls.py              # App URL routes
│   ├── chatbot.py           # Disease information database
│   ├── models.py
│   ├── admin.py
│   ├── apps.py
│   └── tests.py
├── templates/                # HTML templates
│   ├── login.html           # Bootstrap 5 login page
│   └── chatbot.html         # Chatbot interface
├── static/                   # Static files
│   ├── css/
│   │   └── style.css        # Chatbot styling
│   └── js/
│       └── chatbot.js       # Frontend JavaScript
├── manage.py                 # Django management script
└── requirements.txt          # Python dependencies
```

## Usage

1. **Login**: Enter User ID (1234) and Password (gym)
2. **Chat**: Type any disease name (e.g., "diabetes", "fever", "cancer")
3. **Get Information**: The chatbot will provide:
   - Disease explanation
   - Treatment solutions
   - Food recommendations
   - Exercise recommendations

## Supported Diseases
- Cancer
- Diabetes
- Fever
- Headache
- Hypertension
- Asthma
- Arthritis
- Cold

## Technologies Used
- **Backend**: Django 4.2+
- **Frontend**: HTML, CSS, JavaScript
- **UI Framework**: Bootstrap 5
- **Database**: SQLite (default Django database)

## Notes
- This is a demo project for educational purposes
- Disease information is rule-based (dictionary-based)
- Always consult healthcare professionals for medical advice
- Session-based authentication (no database users required)

## Stopping the Server
Press `Ctrl+C` in the terminal where the server is running.

## Deactivating Virtual Environment
```powershell
deactivate
```
