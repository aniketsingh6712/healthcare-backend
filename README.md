
# 🏥 Healthcare Backend API (Django + DRF + PostgreSQL)

This project is a backend system for a Healthcare Application built using Django, Django REST Framework, and PostgreSQL. It includes features for user authentication, patient and doctor management, and patient-doctor assignments.

---

## 📁 Project Structure

```
healthcare_project/
├── authentication/        # Custom User model and JWT auth
│   ├── models.py
│   ├── views.py
│   └── serializers.py
├── patients/              # Patient CRUD operations
├── doctors/               # Doctor CRUD operations
├── mappings/              # Patient-Doctor mapping
├── manage.py
├── .env                   # Environment variables (not committed)
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (`djangorestframework-simplejwt`)
- dotenv for environment configuration

---

## 🛠️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/healthcare-backend.git
cd healthcare-backend
```

2. **Create and Activate Virtual Environment**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**

Create a `.env` file:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=your_db_name
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

5. **Create Database (PostgreSQL)**

Use pgAdmin or CLI to create a database with name `your_db_name`.

6. **Apply Migrations and Run**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # To access Django admin
python manage.py runserver
```

---

## 🔐 Authentication

- **Register**: `POST /api/auth/register/`
- **Login (Get Token)**: `POST /api/auth/login/`  
Returns access and refresh tokens.

Use Authorization header:

```http
Authorization: Bearer <access_token>
```

---

## 📬 API Endpoints

### 🔸 Authentication
- `POST /api/auth/register/` – Register user  
- `POST /api/auth/login/` – Login (get token)

### 🔸 Patients
- `GET /api/patients/` – List user’s patients  
- `POST /api/patients/` – Create patient  
- `GET /api/patients/<id>/` – Get specific patient  
- `PUT /api/patients/<id>/` – Update patient  
- `DELETE /api/patients/<id>/` – Delete patient  

### 🔸 Doctors
- `GET /api/doctors/` – List all doctors  
- `POST /api/doctors/` – Create doctor  
- `GET /api/doctors/<id>/` – Get specific doctor  
- `PUT /api/doctors/<id>/` – Update doctor  
- `DELETE /api/doctors/<id>/` – Delete doctor  

### 🔸 Patient-Doctor Mappings
- `GET /api/mappings/` – List all mappings  
- `POST /api/mappings/` – Assign doctor to patient  
- `GET /api/mappings/patient/<patient_id>/` – Get mappings for a patient  
- `DELETE /api/mappings/<id>/` – Remove doctor from patient  

---

## 📌 Admin Panel

- `http://127.0.0.1:8000/admin/`  
Login using the superuser credentials you created.

---
## .env file
```
SECRET_KEY=your secret
DEBUG=True
DB_NAME=healthcare_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

```

