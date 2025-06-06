from customers.company_customer_liliwelt import Company_customer

print("\n=== Testing Company customer ===\n")

try:
    cc = Company_customer(
        name="Empresa S.A.",
        address="Calle Falsa 123",
        postcode="12345",
        locality="Buenos Aires",
        email="contacto@empresa.com",
        phone="+541112345678",
        password="empresa123",
        company_number="123456789"
    )
    print("Company customer created successfully!")
    print(f"Name: {cc.get_name()}")
    print(f"Company number: {cc.get_company_number()}")
except ValueError as ve:
    print(f"Error: {ve}")