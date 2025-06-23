# Club Management Database Project

This project was developed as part of the KMS+/05/LE_04/01 assignment.  
It consists of a MySQL database that manages all relevant data of a sports club, including players, trainers, teams, training sessions, locations, and education programs.

## Contents

- **SQL Script** (`full_cleaned_club_management.sql`) for:
  - Creating the `club_management` database and all related tables
  - Using surrogate primary keys (`AUTO_INCREMENT`) for intermediate tables
  - Defining **foreign keys** with simplified names
  - Inserting sample data for:
    - Players  
    - Trainers  
    - Teams  
    - Education programs  
    - Training sessions  
    - Training places  
    - Relationships between players-teams and trainers-teams
  - Adding a **trigger** that automatically updates trainer working hours
  - Performing **queries** for data analysis and update operations:
    1. List all players with their teams  
    2. List all trainers with their completed education, grouped by course  
    3. List all players with their trainers and team  
    4. Increase all trainers' salaries by 25%

- **UML Diagram** (`.drawio` file) showing the full database structure

## Notes

- All foreign key constraints were shortened for readability.
- Data insertion follows a strict logical order to respect foreign key dependencies.
- The schema supports many-to-many relationships with proper flexibility.
- Designed for MySQL 8+ with UTF-8 encoding and standard SQL constraints.

## Example Usage

```sql
-- Check if trainer salaries were increased correctly:
SELECT * FROM club_management.trainers;

