from validator_liliwelt import Validator

if __name__ == "__main__":
    # This script tests the validation of customer information using the Validator class

    # -------------------
    # Test email addresses
    # -------------------

    test_emails = [
        "user@example.com",
        "user@domain",
        "user@domain.",
        "user@.com",
        "user@@example.com",
        "user name@example.com",
        "user@domain.com",
        "user@domain..com",
        "@domain.com",
        "user@domain.c",
        "user@domain.toolongtld",
        "u" * 65 + "@example.com",
        "user@" + "a" * 250 + ".com",
        "user@example.com ",
        " user@example.com",
        "." + "user@example.com",
        "user.@example.com",
        "user..name@example.com",
        "user!name@example.com"
    ]

    print("\nTesting emails:\n")
    for email in test_emails:
        result = Validator.validate_email(email)
        print(f"{email:<50} → {'Valid' if result == True else 'Invalid'}")
        assert result in [True, False]

    # -------------------
    # Test phone numbers
    # -------------------

    test_phones = [
        "+43123456789",
        "0043123456789",
        "43123456789",
        "0123456",
        "0123456789012345678901",
        "+43abc56789",
        "0043abc56789",
        "43123abc567",
        "43 12345678",
        "",
        "     "
    ]

    print(""*80)
    print("\nTesting phone numbers:\n")
    for phone in test_phones:
        result = Validator.validate_phone(phone)
        print(f"{phone:<50} → {'Valid' if result == True else 'Invalid'}")
        assert result in [True, False]

    # -------------------
    # Test names
    # -------------------
if __name__ == "__main__":

    test_names = [
        "Ana",
        "Juan Pérez",
        "Jean-Luc",
        "O'Connor",
        " María ",
        "",
        "   ",
        "Pepe123",
        "@Manuel",
        "Laura!",
        "MÜLLER"
    ]

    print("-"*80)
    print("\nTesting names:\n")
    for name in test_names:
        result = Validator.validate_name(name)
        print(f"{name:<50} → {'Valid' if result == True else 'Invalid'}")
        assert result in [True, False]

    # -------------------
    # Test addresses
    # -------------------

    test_addresses = [
        "Calle Falsa 123",
        "Av. Siempre Viva 742",
        "Piso 1°, Depto A",
        "Main Street@",
        "Calle #Principal",
        "",
        "   ",
        "Santa Fé 4568"
    ]

    print("\nTesting addresses:\n")
    for address in test_addresses:
        result = Validator.validate_address(address)
        print(f"{address:<50} → {'Valid' if result == True else 'Invalid'}")
        assert result in [True, False]

    # -------------------
    # Test postcodes
    # -------------------

    test_postcodes = [
        "8010",
        "12345",
        "0001",
        "1234567890",
        "123",
        "12345678901",
        "12A45",
        "123 45",
        "123-45",
        "",
        "     "
    ]

    print("-"*80)
    print("\nTesting postcodes:\n")
    for postcode in test_postcodes:
        result = Validator.validate_postcode(postcode)
        print(f"{postcode:<50} → {'Valid' if result == True else 'Invalid'}")
        assert result in [True, False]

    # -------------------
    # Test localities
    # -------------------

    test_localities = [
        "Graz",
        "Wien",
        "San Miguel de Tucumán",
        "München",
        "São Paulo",
        "Paris123",
        "New York!",
        "@Berlin",
        "",
        "     "
    ]

    print("-"*80)
    print("\nTesting localities:\n")
    for locality in test_localities:
        result = Validator.validate_locality(locality)
        print(f"{locality:<50} → {'Valid' if result == True else 'Invalid'}")
        assert result in [True, False]

    # -------------------
    # Test birthdates
    # -------------------

    test_birthdates = [
        "01.01.2000",
        "31.12.1999",
        "29.02.2000",  # Leap year
        "29.02.2001",  # Not a leap year
        "31.04.2020",  # April has 30 days
        "15.08.2025",  # Future date
        "12/05/2000",
        "2000.05.12",
        "1.1.2000",
        "",
        "    ",
        "32.01.2000",
        "15.13.2000"
    ]

    print("-"*80)
    print("\nTesting birthdates:\n")
    for birthdate in test_birthdates:
        result = Validator.validate_birthdate(birthdate)
        print(f"{birthdate:<50} → {'Valid' if result == True else 'Invalid'}")
        assert result in [True, False]

    # -------------------
    # Test company numbers
    # -------------------

    test_company_numbers = [
        "12345678",
        "123456789",
        "1234567",
        "1234567890",
        "1234A678",
        "12 345678",
        "1234-5678",
        "123",
        "1234567812345678",
        "",
        "        "
    ]

    print("-"*80)
    print("\nTesting company numbers:\n")
    for cn in test_company_numbers:
        result = Validator.validate_company_number(cn)
        print(f"{cn:<50} → {'Valid' if result == True else 'Invalid'}")
        assert result in [True, False]

    # -------------------
    # Test passwords
    # -------------------

    test_passwords = [
        "secret123",  # valid
        "   claveok   ",  # valid (after stripping)
        "12345",  # too short
        "",  # empty
        "      ",  # only spaces
        123456,  # not a string
        None  # NoneType
    ]

    print("-"*80)
    print("\nTesting passwords:\n")
    for password in test_passwords:
        result = Validator.validate_password(password)
        print(f"{repr(password):<50} → {'Valid' if result == True else 'Invalid'}")
        assert result in [True, False]

