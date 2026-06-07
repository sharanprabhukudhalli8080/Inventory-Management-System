# 📦 Inventory Management System

## 📌 Overview

Inventory Management System is a Python and MySQL based command-line application designed to manage product inventory efficiently. The system allows users to perform inventory operations such as adding products, updating stock, searching products, deleting products, and monitoring low-stock items.

---

## 🚀 Features

### 🔐 User Authentication
- User Signup
- User Login
- Credential Validation

### 📦 Product Management
- Add Product
- Update Product Stock
- Delete Product
- Search Product
- View Inventory

### 📊 Inventory Monitoring
- Low Stock Alerts
- Inventory Tracking
- Product Quantity Management

---

## 🛠️ Technologies Used

- Python
- MySQL
- MySQL Connector
- Object-Oriented Programming (OOP)
- CRUD Operations

---

## 📂 Project Structure

```text
Inventory-Management-System/
│
├── main.py
├── operations.py
├── models.py
├── db.py
├── config.py
│
├── requirements.txt
├── README.md

```

---


## ⚙️ Installation

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Database

```sql
CREATE DATABASE inventory_db;
```

### Configure Database

Update `config.py`:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "inventory_db"
}
```

### Run Application

```bash
python main.py
```

---

## 📋 Functionalities

### User Management
- Create Account
- Login Authentication

### Inventory Operations
- Add New Products
- Update Product Quantity
- View Available Inventory
- Search Products
- Delete Products

### Stock Monitoring
- Identify Low Stock Products
- Inventory Status Tracking

---

## 🎯 Learning Outcomes

- Python Programming
- Database Connectivity
- MySQL Integration
- CRUD Operations
- Exception Handling
- Modular Programming
- Authentication Systems

---

## 🔮 Future Enhancements

- Password Encryption
- GUI using Tkinter
- Inventory Analytics Dashboard
- Sales Management Module
- Barcode Integration
- Export Reports to Excel

---

## 👨‍💻 Author

**Sharanprabhu Kudhalli**

Computer Science Engineering Student | Aspiring Data Analyst | Python & Data Science Enthusiast

---

⭐ If you found this project useful, please consider giving it a star.
