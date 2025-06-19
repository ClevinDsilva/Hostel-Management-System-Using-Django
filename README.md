# 🏠 Hostel Management System using Django

A web-based Hostel Management System built using the **Django framework**. This project provides a complete solution for managing hostel operations such as room allocation, tenant records, staff management, and admin functionalities.

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, Bootstrap
- **Backend:** Python, Django
- **Database:** MySQL
- **Server:** Apache (optional for deployment)

---

## 📁 Project Structure

![image](https://github.com/user-attachments/assets/2285c9b6-268c-4004-aff3-13834de2b75d)


---

## ✨ Features

### 👩‍💼 Admin Module
- Admin login and dashboard
- Add/edit/delete staff
- Add/edit/delete tenant records
- Assign rooms to tenants
- View hostel occupancy stats

### 👨‍🔧 Staff Module
- Staff login
- View tenant list
- Handle maintenance and complaints
- Update tenant status

### 🧑‍🎓 Tenant Module
- Tenant login
- View room and profile details
- Lodge complaints or requests
- Track hostel stay history

---

## 🚀 Getting Started

### 📦 Prerequisites
- Python 3.x
- pip
- MySQL
- Django (`pip install django`)

### 🔧 Installation

1. **Clone the Repository**

# bash
git clone https://github.com/ClevinDsilva/Hostel-Management-System-Using-Django.git
cd Hostel-Management-System-Using-Django

# Create Virtual Environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt  # If provided

# Configure Database

Update settings.py to use MySQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Run Migrations and Create Superuser

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Start the Server

python manage.py runserver

python manage.py runserver

# Project Dic

[Django min project.pdf](https://github.com/user-attachments/files/20822655/Django.min.project.pdf)
