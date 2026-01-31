# SRH Project Nexus API

Sexual Reproductive Health Education and Services to Adolescents API.

## Overview
This API provides a centralized system to manage adolescents, SRH sessions, services offered, and feedback.

## Setup

1. **Prerequisites**
   - Python 3.x
   - Virtual Environment (recommended)

2. **Installation**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Database Setup**
   ```bash
   python manage.py migrate
   ```

4. **Run Server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `GET /api/users/` - List users
- `GET /api/adolescents/` - List adolescents
- `POST /api/adolescents/` - Register new adolescent
- `GET /api/locations/` - List locations
- `GET /api/sessions/` - List sessions
- `GET /api/services/` - List services
- `GET /api/service-records/` - List service usage history
- `POST /api/feedback/` - Submit feedback

## Models

- **User**: Staff and Adolescents (differentiated by role).
- **Location**: Health facilities.
- **Session**: Educational sessions at a location.
- **Service**: Types of services available.
- **ServiceRecord**: Individual record of a service provided to an adolescent.
- **Feedback**: Ratings and comments.
# srh-project-nexus
