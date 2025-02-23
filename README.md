
# Gas Utility Consumer Services

## Overview
This Django application is designed to help a gas utility company manage customer service requests efficiently. It allows customers to submit service requests online, track their status, and manage their account information. Customer support representatives can also use the application to manage requests and provide support to customers.

The application includes features such as user authentication, service request management, profile management, and file uploads for service requests.

---

## Features

### For Customers:
1. **User Authentication**:
   - Sign up, log in, and log out.

2. **Service Requests**:
   - Submit new service requests with details and file attachments (e.g., images).
   - View a list of all submitted service requests.
   - Track the status of service requests (e.g., Pending, In Progress, Resolved).
   - Update or delete service requests.

3. **Profile Management**:
   - Update profile information (e.g., name, email, phone number).
   - Add or update a profile picture.

---

## Tech Stack
- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, Bootstrap
- **Authentication**: Django Authentication System
- **File Uploads**: Django's `FileField` and `ImageField`

---

## Application Structure
The Django project is structured as follows:

```
gas_utility_portal/
├── accounts/                  # Handles user authentication and profile management
│   ├── models.py              # User and Profile models
│   ├── views.py               # Views for login, signup, profile, etc.
│   ├── forms.py               # Forms for user registration and profile updates
│   ├── urls.py                # URLs for authentication and profile management
│   └── templates/             # HTML templates for authentication and profile pages
│
├── service_requests/          # Handles service request management
│   ├── models.py              # ServiceRequest model
│   ├── views.py               # Views for creating, viewing, updating, and deleting requests
│   ├── forms.py               # Forms for service requests
│   ├── urls.py                # URLs for service request management
│   └── templates/             # HTML templates for service request pages
│
├── static/                    # Static files (CSS, JavaScript, images)
│   ├── css/                   # Custom CSS files
│   └── images/                # Uploaded images and profile pictures
│
├── templates/                 # Base templates and global HTML files
│   ├── base.html              # Base template for all pages
│   └── includes/              # Reusable template components (e.g., navbar, footer)
│
├── config/                    # Main project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
│   └── wsgi.py                # WSGI configuration
│
├── manage.py                  # Django management script
└── requirements.txt           # Python dependencies
```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/register/` | POST | User registration |
| `/login/` | POST | User login |
| `/logout/` | GET | User logout |
| `/profile/` | GET/PUT | View and update profile |
| `/requests/` | GET | View all service requests |
| `/requests/create/` | POST | Create a new request |
| `/requests/<id>/` | GET/PUT/DELETE | View, update, or delete a request |
---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- PostgreSQL
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/gas-utility-portal.git
cd gas-utility-portal
```

### Step 2: Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure PostgreSQL
1. Create a PostgreSQL database:
   ```bash
   createdb gas_utility_portal
   ```
2. Update the database settings in `gas_utility_portal/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'gas_utility_portal',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### Step 5: Run Migrations
```bash
python manage.py migrate
```

### Step 6: Create a Superuser
```bash
python manage.py createsuperuser
```

### Step 7: Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to access the application.

---

## Screenshots




---




