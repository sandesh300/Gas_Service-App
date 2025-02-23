# Gas Utility Portal

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
![Screenshot (120)](https://github.com/user-attachments/assets/aaf52aac-1e0c-4863-b705-bcb4600ef4db)
![Screenshot (121)](https://github.com/user-attachments/assets/c730db24-3b22-48e9-ae48-26218d563cbf)
![Screenshot (122)](https://github.com/user-attachments/assets/96138f31-9544-4a49-9ec1-c1eab33373cd)
![Screenshot (123)](https://github.com/user-attachments/assets/9c8b7f26-1932-4b68-9285-5774916c6193)
![Screenshot (124)](https://github.com/user-attachments/assets/0295ce6b-40f8-4569-905e-e7bf4206672d)
![Screenshot (125)](https://github.com/user-attachments/assets/5ef7ee0d-1b24-43b0-8b49-ed6b96d70b31)

![Screenshot (127)](https://github.com/user-attachments/assets/0523456e-8e56-4fda-8f82-d0888d7f0a98)
![Screenshot (129)](https://github.com/user-attachments/assets/7ef2280a-7e7e-49c7-bff0-878b0a5fbda3)
![Screenshot (130)](https://github.com/user-attachments/assets/12b77742-3166-4b9c-bba4-1a859a1cfdca)
![Screenshot (131)](https://github.com/user-attachments/assets/3649fef2-eced-4489-b3df-022b2d37807e)







---




