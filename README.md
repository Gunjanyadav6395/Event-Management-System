# Event Management System

A full-stack web-based **Event Management System** built with **Python, Django, Bootstrap 5, JavaScript, and SQLite**. The application provides role-based functionality for administrators and users to create and manage events, categories, registrations, members, wishlists, ticket verification, and event-related activities through a responsive web interface.

The project also includes an **AI-powered chatbot using Google Gemini API** to provide event-related assistance.

## ✨ Features

### 👨‍💼 Admin Features

* Secure admin authentication
* Admin dashboard with event statistics
* Event creation, editing, and deletion
* Event category management
* Event member/registration management
* Event status and priority management
* Event notifications
* Ticket and attendee management
* QR-based ticket scanning and verification
* Check-in tracking with check-in time
* Responsive admin dashboard
* Customizable navbar and sidebar themes

### 👤 User Features

* User registration and login
* User logout
* User profile management
* Browse available events
* View detailed event information
* Register for events
* View registered events
* Wishlist events
* Ticket-related functionality
* Event participation/check-in support
* Change password
* Forgot password and password reset functionality

### 🤖 AI Chatbot

The project includes an AI-powered chatbot integrated with the **Google Gemini API**.

The chatbot is designed to assist users with event-related information and provide an interactive way to communicate with the application.

> The Gemini API key is stored through an environment variable and is not committed to the repository.

---

## 🛠️ Tech Stack

| Technology            | Purpose                                    |
| --------------------- | ------------------------------------------ |
| **Python**            | Backend programming                        |
| **Django**            | Web framework and application architecture |
| **SQLite**            | Development database                       |
| **HTML5**             | Page structure                             |
| **CSS3**              | Custom styling                             |
| **JavaScript**        | Client-side functionality                  |
| **Bootstrap 5**       | Responsive UI                              |
| **Crispy Forms**      | Django form rendering                      |
| **Pillow**            | Image processing                           |
| **Google Gemini API** | AI chatbot functionality                   |
| **Git & GitHub**      | Version control                            |

---

## 🏗️ Project Architecture

The application follows the **Django MVT (Model-View-Template)** architecture.

```text
Event-Management-System/
│
├── chatbot/
│   ├── views.py
│   └── ...
│
├── event_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
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
│   ├── base/
│   └── ...
│
├── manage.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🔐 Authentication & Authorization

The application provides separate functionality for administrators and regular users.

### Authentication

* User registration
* User login/logout
* Password change
* Forgot password
* Password reset flow

### Authorization

Different application areas and actions are available based on the user's role, providing separate experiences for administrators and regular users.

---

## 🎟️ Event & Ticket Management

The system supports the complete event management workflow:

```text
Create Event
     ↓
Publish / Manage Event
     ↓
Users Browse Event
     ↓
User Registration
     ↓
Event Member / Attendee Management
     ↓
Ticket Verification
     ↓
Event Check-in
```

Administrators can manage event members and verify tickets using the application's ticket verification functionality.

---

## 🤖 Gemini AI Configuration

The chatbot uses the **Google Gemini API**.

The API key should be stored in an environment variable rather than directly inside the source code.

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Do **not** commit the `.env` file to GitHub.

The repository already uses `.gitignore` to keep environment-specific secrets out of version control.

---

## 🚀 Installation & Setup

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

#### Windows PowerShell

```powershell
.\env\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
env\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file and add the required configuration:

```env
GEMINI_API_KEY=your_api_key_here
```

### 7. Apply database migrations

```bash
python manage.py migrate
```

### 8. Create an admin/superuser

```bash
python manage.py createsuperuser
```

Follow the instructions displayed in the terminal.

### 9. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

---

## 🗄️ Database

The project currently uses **SQLite** as the development database.

Database migrations are maintained inside the Django application's `migrations` directory.

The SQLite database file is excluded from version control through `.gitignore`.

For production deployment, the project can be configured with a production-ready database such as PostgreSQL.

---

## 📁 Important Django Components

| Component     | Responsibility                         |
| ------------- | -------------------------------------- |
| `models.py`   | Database models and relationships      |
| `forms.py`    | Django forms and validation            |
| `views.py`    | Application logic and request handling |
| `urls.py`     | URL routing                            |
| `templates/`  | HTML user interface                    |
| `static/`     | CSS, JavaScript, and static images     |
| `migrations/` | Database schema migrations             |
| `settings.py` | Django configuration                   |
| `chatbot/`    | Gemini-powered chatbot functionality   |

---

## 📸 Screenshots

Screenshots can be added here to showcase the main interfaces of the application.

Recommended screenshots:

* Home page
* User registration/login
* User dashboard
* Event listing
* Event details
* Wishlist
* Registered events
* Admin dashboard
* Event management
* Category management
* Event member management
* QR/ticket verification
* AI chatbot

---

## 🎯 Technical Highlights

This project demonstrates practical implementation of:

* Django MVT architecture
* Django ORM and relational database modeling
* CRUD operations
* Form handling and validation
* Authentication and authorization
* Template inheritance
* Static and media file management
* Responsive UI development with Bootstrap
* Event registration and member management
* Ticket verification and check-in workflow
* QR-based functionality
* AI API integration using Google Gemini
* Environment-variable based configuration
* Database migrations
* Git and GitHub version control

---

## 🔮 Future Enhancements

Potential future improvements include:

* Online payment gateway integration
* Automated email notifications
* Advanced event search and filtering
* Event analytics and reporting
* REST API development
* PostgreSQL production deployment
* Cloud deployment
* Multi-organizer/event-host support
* Advanced role and permission management
* Downloadable PDF tickets

---

## 🔒 Security Notes

* API keys and sensitive credentials should be stored in environment variables.
* `.env` should never be committed to GitHub.
* `DEBUG` should be disabled in production.
* `SECRET_KEY` should be kept private.
* `ALLOWED_HOSTS` should be configured appropriately for deployment.
* Production deployments should use secure HTTPS configuration.

---

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

* Python and Django development
* Backend application architecture
* Database design and Django ORM
* Authentication systems
* CRUD-based application development
* Frontend integration with Django templates
* Responsive web design
* API integration
* AI feature integration
* Git/GitHub workflow
* Environment-based application configuration

---

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

---

## 👩‍💻 Author

**Gunjan Yadav**

MCA Graduate | Python & Django Developer

GitHub: [Gunjanyadav6395](https://github.com/Gunjanyadav6395)

---

⭐ If you find this project useful or interesting, consider giving the repository a star.
