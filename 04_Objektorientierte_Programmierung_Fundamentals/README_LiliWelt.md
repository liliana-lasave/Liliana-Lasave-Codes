
# WarenWelt Online Shop Project

This project is part of the KMS+/04/LE_03 series and consists of a complete modular implementation of an online shop system in Python using Object-Oriented Programming (OOP). It is developed in three stages:

---

## Part 1: Customer Management (`KMS+/04/LE_03-01`)

- Implementation of a base class `Customer`
- Subclasses: `PrivateCustomer` and `CompanyCustomer`
- A `Validator` class for input validation:
  - Email, phone, name, address, birthdate, company number
- Automatic ID assignment
- Age calculation method (`PrivateCustomer`)
- All data validated in constructors
- Organized into separate Python modules
- UML diagram showing inheritance and validation
- `test_classes_liliwelt.py` demonstrates valid and invalid inputs

---

## Part 2: Product Management & Data Storage (`KMS+/04/LE_03-02`)

- Abstract base class: `Product`
- Concrete subclasses:
  - `PrivateLesson`
  - `GroupWorkshop`
  - `Course`
- Each class implements a `get_info()` method
- Shared methods: `add_rating`, `average_rating`
- Class `Storage` to interact with SQLite DB:
  - Store/load customers and products
- Exception hierarchy: `DatabaseError`, `ConnectionError`, etc.
- Multiple test files for CRUD operations and DB integration

---

## Part 3: Shopping Cart & Order System (`KMS+/04/LE_03-03`)

- Class `ShoppingCart`:
  - Attributes: customer, products, total
  - Methods: `add_product()`, `remove_product()`, `clear_cart()`, `calculate_total()`
  - Automatic 5% discount for company customers
- Class `Order`:
  - Attributes: timestamp, products, customer_data, total_amount
  - Method `generate_invoice()` creates `.txt` receipt
- Integrated with customer and product modules
- `test_order_process.py` demonstrates full flow
- Invoice example generated: `invoice_test.txt`

---

## Project Structure

```
/customers
/products
/orders
/errors
/validation
/tests
/diagrams
```

---

## Features

- Clean and modular OOP structure
- Abstract and inherited classes
- Input validation
- SQLite integration
- Custom exception handling
- UML diagrams
- Test scripts for each project phase

---

## Files for Submission

- UML diagrams in `.drawio`
- Full Python implementation
- SQL DB: `liliwelt.db`
- Test files with complete workflows
- This README file

---

Project developed by **Liliana Lasave** for the WarenWelt Online Shop Simulation.
