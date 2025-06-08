# LiliWelt - Online Shop with Tkinter

This is the final part of the WarenWelt project (KMS+/04/LE_03-04).  

It is a simple desktop application created with Python and Tkinter.

The app allows users to register, log in, view products, add them to a cart, and place an order.

## Technologies

- Python
- Tkinter
- SQLite (local database)

## Project Structure

main.py              -> Starts the app  
gui/                 -> Screens: login, register, catalog, cart, checkout  
customers/           -> Customer classes  
products/            -> Product categories  
orders/              -> Order saving  
database/            -> Load and save data  
validation/          -> Input checks  
diagrams/            -> Mockups  
liliwelt.db          -> The database

## How the app works (User flow)

1. The user opens the app.
2. They can log in or register.
3. They see a catalog of products and can filter them.
4. They can add products to the cart.
5. In the cart, they can review or remove items.
6. At checkout, they choose a delivery method and confirm the order.
7. The order is saved, and they return to the catalog.

## Test Cases (examples)

- Try to register with valid data → should work
- Try to register with wrong email → should show error
- Try to login with good data → should go to catalog
- Try to login with wrong password → should show error
- Add and remove products → cart updates correctly
- Confirm order with delivery → order is saved

## How to run it

1. Open the terminal
2. Go to the project folder
3. Run:

```
python gui/main.py
```

## Notes

This project was created for the course KMS+/04/LE_03-04.  
It is part of the WarenWelt series.
