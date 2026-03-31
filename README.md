### 📌 Overview

The Hospital Management System (HMS) is a Python-based application designed to manage hospital operations efficiently using Object-Oriented Programming (OOP) principles.

The system provides both Graphical User Interface (GUI) and Command Line Interface (CLI) support, enabling flexible interaction for managing patients, doctors, and billing processes.

It integrates with a MySQL database to store and retrieve data in a structured and reliable manner.

### ✨ Features
🔐 Secure Login Authentication System
🧑‍⚕️ Add, View, and Delete Patient Records
👨‍⚕️ Add Doctor Details and Manage Specializations
🔗 Assign Doctors to Patients
📋 View Patient and Doctor Information
💰 Generate Billing Details
🖥️ Dual Interface Support (GUI + CLI)
🗄️ Persistent Data Storage using MySQL
🛠️ Tech Stack

### Programming Language:
Python

### GUI Framework:
Tkinter / CustomTkinter

### Interface: 
CLI and GUI

### Database:
MySQL

###Architecture:
Object-Oriented Programming (OOP)

### 📁 Project Structure
Hospital-Management/
│
├── main.py           # CLI-based system
├── main_gui.py       # GUI-based system
├── login.py          # Login interface
├── database.py       # Database connection
│
├── model/            # OOP-based modules
│   ├── person.py
│   ├── patient.py
│   ├── doctor.py
│   └── billing.py
│
├── images/           # UI images
└── docs/             # Documentation (optional)

### ⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/hospital-management-system.git
cd hospital-management-system
2️⃣ Create Virtual Environment (Optional)
python -m venv .venv

### Activate:

Windows:
.venv\Scripts\activate
Linux/Mac:
source .venv/bin/activate

### 3️⃣ Install Dependencies
pip install customtkinter mysql-connector-python

### 4️⃣ Configure Database
Ensure MySQL server is running
Create a database named:
hospital_db
Create required tables (patients, doctors, etc.) using your SQL script or manually

### 5️⃣ Run the Application
### ▶️ GUI Version:
python login.py
### ▶️ CLI Version:
python main.py

### 🔑 Default Login Credentials
Username: admin@hms.com
Password: 1234

(Can be modified in login.py)

### 🧠 Core Concepts Used
Object-Oriented Programming:
Inheritance
Encapsulation
Modularity

### Database Integration:
MySQL with Python (mysql-connector-python)

### User Interface Design:
Tkinter GUI
CLI-based interaction

### Software Design:
Separation of concerns
Modular architecture

### 📊 Functional Modules
Patient Management
Add, delete, and view patient records
Doctor Management
Store doctor details and specialization
Doctor Assignment
Link doctors with patients
Billing System
Generate bills based on patient stay and charges
🚀 Future Enhancements
🌐 Convert to Web Application using Flask/Django
📱 Mobile App Integration
📊 Dashboard with Analytics
🔒 Advanced Authentication (JWT / OAuth)
☁️ Cloud Deployment support
