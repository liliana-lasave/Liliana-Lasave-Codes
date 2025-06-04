from private_customers_liliwelt import Private_customer

# Create a test object

priv_cost = Private_customer(

    name="Lili",

    address="Calle Falsa 123",

    postcode="8010",

    locality="Graz",

    email="lili@example.com",

    phone="+436601234567",

    password="Hola123",

    birthdate="27.03.1979"

)

print("Birthdate:", priv_cost.get_birthdate())

print("Age:", priv_cost.get_age())

