
# 🏦 BANK OF BHOPAL – Python CLI Banking Management System
A CLI-based banking system inspired by real-world banking operations of **BANK OF BHOPAL**.

A **production-inspired, learning-driven CLI Banking System** built using **Python and MySQL**, designed to **revise and strengthen backend fundamentals** such as **Object-Oriented Programming (OOPs)**, **Python Database Connectivity (PDBC)**, and **exception handling** through a real-world banking simulation.

This project focuses on **clarity of concepts, clean architecture, and practical implementation** rather than just UI.

---

## 🎯 Why This Project?

The primary purpose of building this project was to:

- Revise **OOPs concepts** using real-world entities (Account, Customer, Bank)
- Practice **Python–MySQL connectivity (PDBC)**
- Implement **custom exception handling**
- Apply **input validations** and business rules
- Understand **modular and scalable code design**
- Convert theoretical knowledge into **hands-on backend experience**

> 💡 *Built with the mindset: “If I can design backend logic here, I can scale it to APIs later.”*

---

## ✨ Key Features

### 👤 Customer Features
- Account creation with validations  
- Secure PIN-based authentication  
- Deposit money  
- Withdraw money  
- Balance enquiry  
- View account details  

### 🛠️ Admin / Bank Features
- Employee authentication  
- View all customer records  

### ⚙️ System Features
- Modular codebase (separate files for each responsibility)  
- Custom exception handling  
- Input validation layer  
- Database-driven persistence  
- CLI-based interactive menu  

---

## 🧠 Core Concepts Implemented

- Object-Oriented Programming (OOPs)
- Python Database Connectivity (PDBC)
- Exception Handling
- Input Validation
- Modular Architecture
- Real-world business logic handling

---

## 🛠️ Tech Stack

| Technology | Usage |
|----------|------|
| Python | Core programming |
| MySQL | Database |
| mysql-connector-python | DB connectivity |
| python-dotenv | Secure environment variables |
| NumPy | Account number generation |

---

## 📁 Project Structure
Banking-System/
│
├── Account.py # Account creation logic
├── Balance_Enquiry.py # Balance enquiry functionality
├── Customer.py # Bank/Admin operations
├── CustomerInfo.py # Customer account details
├── dbConnect.py # MySQL database connection
├── Deposit.py # Deposit functionality
├── Withdraw.py # Withdraw functionality
├── Validations.py # Input validations
├── Exceptions.py # Custom exception definitions
├── Main.py # Menu-driven CLI functionality
├── Test.py # Application entry point
└── README.md # Project documentation

---

## 🗄️ Database Schema

### Database: `Customer`

### Table: `Customer_Info`

| Column | Type |
|------|------|
| acc_no | BIGINT (Primary Key) |
| cname | VARCHAR(100) |
| bal | FLOAT |
| pin | INT |

---

## 🔐 Security Best Practices

- Database credentials stored using **environment variables**
- `.env` file excluded from version control
- No hardcoded passwords in source code

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Thakur_Pradeep/banking-system.git
cd banking-system
