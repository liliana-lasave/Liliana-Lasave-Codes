# LiliWelt Onlineshop – KMS+/04/LE_03-02

## Project Overview

This project is an online shop for music courses, developed as part of the "Object-Oriented Programming" module.
It fulfills all the requirements of the assignment KMS+/04/LE_03-02.

## Contents

### 🧱 Product Hierarchy
- **Product** (abstract class)
  - `PrivateLesson`: includes teacher and instrument
  - `GroupWorkshop`: includes theme and max participants
  - `Course`: includes number of sessions and certificate

### 💾 Database
- SQLite database `liliwelt.db`
- Tables: `private_lessons`, `group_workshops`, `courses`

### 🗃 Storage Class
- `Storage`: manages all connections and operations with the database
- Supports: `connect`, `disconnect`, `save`, `load`, `load_all`, `create_tables`

### ⚠️ Exception Handling
- Custom exception classes: `DatabaseError`, `ConnectionError`, `SaveError`, `NotFoundError`

### 🧪 Tests
- `test_insert_all.py`: saves example data to the database
- `test_show_all_products.py`: displays all saved data
- `test_classes_liliwelt.py`: validates user input

### 📊 UML Diagram
The UML diagram is located at:
```
diagrams/Lasave_KMS+_04_LE_03_02_liliwelt_UML.drawio
```

## Submission
- All required elements from the task description are included.
- The project is fully documented and tested.
