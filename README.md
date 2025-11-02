# Mon projet

# 🏋️‍♂️ SportClub Management System

This project demonstrates the use of **Object-Oriented Programming (OOP)** and the **SOLID principles** through a simple sport club management system.  
It handles **Members**, **Events**, and **Subscriptions**, and integrates them in the `SportClub` main class.

---

## ⚙️ Project Structure

Each class is responsible for one specific type of data and functionality.

---

## 🧩 Applied SOLID Principles

### 1. **Single Responsibility Principle (SRP)**

**Applied in:** `Members`, `Events`, and `Subscription` classes  
**Explanation:**  
Each class has **only one reason to change** — for example:

- `Members.py` only manages member data.
- `Events.py` only handles event-related information.
- `Subscription.py` only manages payments and subscriptions.

**Problem solved:**  
This separation avoids code duplication and makes the program easier to maintain and test.

---

### 2. **Open/Closed Principle (OCP)**

**Applied in:** `SportClub` class methods like `load_data()` and `display_data()`  
**Explanation:**  
The code is **open for extension** (you can add new entities like `Coach` or `TrainingSession`)  
but **closed for modification** (you don’t need to edit existing logic).

**Problem solved:**  
Adding new features doesn’t require changing the main program — reducing the risk of introducing bugs.

---

### 3. **Liskov Substitution Principle (LSP)**

**Applied conceptually in:** future extensions (e.g., subclasses of `Member` such as `StudentMember` or `CoachMember`)  
**Explanation:**  
Any subclass can replace the parent class without altering program behavior.

**Problem solved:**  
Ensures consistent behavior when using polymorphism in future enhancements.

---

### 4. **Interface Segregation Principle (ISP)**

**Applied in:** the design choice to keep `Members`, `Events`, and `Subscription` independent.  
**Explanation:**  
Each class only implements the methods it actually needs — there are no “fat” or unnecessary interfaces.

**Problem solved:**  
Improves clarity and prevents classes from depending on unused code.

---

### 5. **Dependency Inversion Principle (DIP)**

**Applied in:** the interaction between `SportClub` and data sources (CSV files).  
**Explanation:**  
The `SportClub` class depends on **abstract operations** (like `load_data()` or `save_data()`),  
not on the concrete CSV implementation — meaning you could switch to a database easily.

**Problem solved:**  
Improves flexibility and scalability of the system for future data storage options.

---

## 🧠 Summary

| Principle | Where Applied                | Problem Solved                     |
| --------- | ---------------------------- | ---------------------------------- |
| SRP       | Each entity class            | Simplifies maintenance             |
| OCP       | `SportClub` management logic | Add features without breaking code |
| LSP       | Potential subclassing        | Ensures substitutability           |
| ISP       | Independent entities         | Prevents unused dependencies       |
| DIP       | Data handling abstraction    | Allows flexibility in data sources |

---
