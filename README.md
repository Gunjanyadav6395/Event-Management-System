# Event Management System

A web-based Event Management System built with **Python, Django, Bootstrap 5, and SQLite**. The system provides separate functionality for administrators and users to manage events, categories, registrations, members, and related event information through a responsive web interface.

## Features

### Admin Features

- Admin authentication
- Admin dashboard
- Event category management
- Create, edit, and delete event categories
- Event management
- Create, edit, and delete events
- Event member management
- Event member listing
- Event status and priority management
- Dashboard statistics
- Notifications
- Responsive admin interface
- Navbar and sidebar navigation
- Theme customization for navbar and sidebar

### User Features

- User registration
- User login and logout
- User dashboard
- Browse available events
- Event information and details
- Event registration/member functionality
- Event wishlist functionality
- Password change
- Forgot password and password reset flow

## Tech Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Backend programming       |
| Django       | Web framework             |
| SQLite       | Database                  |
| HTML5        | Page structure            |
| CSS3         | Styling                   |
| JavaScript   | Client-side functionality |
| Bootstrap 5  | Responsive UI             |
| Crispy Forms | Django form rendering     |
| Pillow       | Image handling            |
| Git & GitHub | Version control           |

## Project Structure

```text
Event-Management-System/
│
├── events/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── base/
│
├── manage.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Gunjanyadav6395/Event-Management-System.git
```

### 2. Navigate to the project directory

```bash
cd Event-Management-System
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\env\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an admin/superuser

```bash
python manage.py createsuperuser
```

Follow the instructions shown in the terminal.

### 8. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Configuration

Before deploying the project to production, configure the following appropriately:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- Database configuration
- Email configuration
- Static and media file settings

Sensitive credentials and environment-specific configuration should not be committed to GitHub.

## Authentication

The project includes authentication-related functionality such as:

- User registration
- User login
- Logout
- Password change
- Forgot password
- Password reset

Email-based password reset can be configured using an appropriate email service for production.

## Database

The project currently uses **SQLite** for development.

The database file is intentionally excluded from version control through `.gitignore`.

## Future Enhancements

Planned improvements may include:

- Digital ticket generation
- Downloadable PDF tickets
- QR-code based event check-in
- Online payment integration
- Email notifications
- Advanced event search and filtering
- Event analytics and reporting
- REST API
- React-based frontend
- Cloud deployment
- Multi-organizer/event-host support

## Screenshots

Screenshots of the application will be added here to demonstrate the main interfaces, including:

- Login page
- Admin dashboard
- User dashboard
- Event list
- Create event page
- Event category management
- Event member management

## Learning Objectives

This project demonstrates practical implementation of:

- Django MVT architecture
- Database modeling with Django ORM
- CRUD operations
- Django forms
- Authentication and authorization
- Template inheritance
- Static and media file handling
- Bootstrap-based responsive design
- Git and GitHub version control

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Author

**Gunjan Yadav**

MCA Graduate | Python & Django Developer

---

⭐ If you find this project useful, consider giving the repository a star.
