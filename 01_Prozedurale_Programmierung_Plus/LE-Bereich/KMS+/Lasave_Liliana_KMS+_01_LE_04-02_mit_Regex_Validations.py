


from datetime import datetime
import re

# ---------------------- CLEANING FUNCTIONS ----------------------

def clean_input(instring):
    """
        Removes leading/trailing whitespace and collapses multiple spaces into one.
        Used for general text like names or addresses.

        Args:
            instring (str): Input string to clean.

        Returns:
            str: Cleaned string.
        """
    clean_list = instring.strip().split()   # Split and remove whitespace
    clean_string = ' '.join(clean_list)     # Rejoin with single spaces
    return clean_string

def clean_email_input(instring):
    """
       Light cleaning for emails: only removes leading/trailing spaces.
       Preserves internal formatting (e.g., '+' in Gmail addresses).

       Args:
           instring (str): Email input to clean.

       Returns:
           str: Stripped email string.
       """
    return instring.strip()


# ---------------------- DISPLAY FUNCTION ----------------------
def print_users_data(name, address_street, address_town, birth_date, phone, email):
    """
       Prints user data in a consistent, readable format.

       Args:
           name (str): User's full name.
           address_street (str): Street address.
           address_town (str): Town and postcode.
           birth_date (str): Date in dd/mm/yyyy format.
           phone (str): 10-digit phone number.
           email (str): Validated email address.
       """
    print("\n")
    print("The user's information:")
    print("Name     :", name)
    print("Address  :", address_street)
    print("         :", address_town)
    print("Birthdate:", birth_date)
    print("Phone    :", phone)
    print("Email    :", email)


# ---------------------- DATA COLLECTION FUNCTIONS ----------------------

def get_name():
    """
    Prompts the user to input their first and last name, and validates the input.

    The validation criteria are as follows:
      - The input must consist of exactly two words (one for the first name and one for the last name).
      - Each word must contain only letters. Valid characters include:
          • Standard alphabetical letters (A-Z and a-z)
          • Accented characters (e.g., Á, é, í, ó, ú)
          • The Spanish letter Ñ (both uppercase and lowercase)
          • Letters with diacritics (e.g., Ä, Ë, Ï, Ö, Ü and their lowercase variants)
          • Hyphens (-) and apostrophes (') are allowed within each word.
      - Extra spaces are trimmed and collapsed to ensure proper formatting before validation.

    Returns:
        str: The cleaned full name in the format "First Last" if the validation criteria are met.
    """

    error_found = True

    # Pattern for first or last name: letters (including accents and ñ), optionally followed by a hyphen or apostrophe and more letters.
    pattern_name = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÄËÏÖÜäëïöü]+(?:[-'][A-Za-zÁÉÍÓÚáéíóúÑñÄËÏÖÜäëïöü]+)?$")

    while error_found == True:
        name = input("Enter your first and last name separated by a space: ")  # only basic validation: checks if name has two parts
        name = clean_input(name)
        name_list = name.split()
        if len(name_list) != 2:
            print("Must enter only first and last name.")
        else:
            if pattern_name.fullmatch(name_list[0]) and pattern_name.fullmatch(name_list[1]):
                error_found = False
            else:
                print ("The first and last name must contain only letters (accents, hyphens and apostrophes may be included).")

    return name
# ---------------------------


def get_phone():
    """
    Requests and validates the phone number:
    - Must contain exactly 10 digits.
    A regular expression is used for validation.
    """

    error_found = True
    pattern_phone = re.compile(r"^\d{10}$")  # Only 10 digits without spaces or symbols.

    while error_found == True:
        phone = input("Enter your 10-digit phone number (no spaces or dashes): ")
        phone = clean_input(phone)
        if not pattern_phone.fullmatch(phone):
            print("The telephone number must contain exactly 10 digits.")
        else:
            error_found = False

    return phone
# ---------------------------


def get_birth_date():
    """
       Requests the date of birth in dd/mm/yyyy format and validates it using datetime.
    """
    error_found = True

    while error_found == True:
        birth_date = input("Enter the birthdate with the format dd/mm/yyyy: ")

        try:
            datetime.strptime(birth_date, "%d/%m/%Y")
            error_found = False
        except ValueError:
            print("Invalid date. Be sure to use the format dd/mm/yyyy.")

    return birth_date
# ---------------------------


def get_address_street():
    """
        Requests an address from the user.
        Verifies that the address is not empty.
        Ensures that the address has at least two parts (e.g. “Number” and “Street”).
        Validates that the address includes only alphanumeric characters, spaces and some symbols allowed by a regular expression.
        It allows executing a loop that repeats until a valid entry is obtained.
        All in all, the code ensures that the entered address has an acceptable format before being used later in the program.
    """

    error_found = True

    # Pattern allows letters, numbers, spaces, and common address symbols
    pattern_address = re.compile(r"^[\wÁÉÍÓÚáéíóúÑñÄËÏÖÜäëïöü\s\.,'-]+$")

    while error_found:
        address_street = input("Enter your street address (e.g., '123 Main St' or 'Main Street'): ")
        address_street = clean_input(address_street)

        if not address_street:
            print("Error: Address cannot be empty.")
        elif len(address_street.split()) < 2:
            print("Error: Please include both street number and name (e.g., '123 Main St').")
        elif not pattern_address.fullmatch(address_street):
            print("Error: Only letters, numbers, spaces, and .,-' are allowed.")
        else:
            error_found = False

    return address_street
# ---------------------------


def get_email():
    """
        Validates email addresses with:
        - Regex pattern for format
        - Length checks (RFC 5321 compliant)
        - Exactly one '@'

        Returns:
            str: Validated email address.
        """
    # Regex pattern for final validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    error_found = True

    while error_found:
        email = input("Enter your email: ")
        email = clean_email_input(email)

        # Validate total length
        if len(email) > 254:
            print("Email is too long (max 254 characters)")
            # print(f"Email length = {len(email)}")  # Uncomment for debugging
            continue


        # Validate that it contains exactly one '@' in order to be able to split it
        if email.count('@') != 1:
            print("The email must contain exactly one '@'")
            continue

        username, domain = email.split('@')

        # Validate the length of the username (before the '@')
        if len(username) > 64:
            print ("The part of the email before the '@' is too long (max. 64 characters)")
            print(f"DEBUG: Username's length = {len(username)}")
            continue

        # Validate the length of the domain (after the '@')
        if len(domain) > 189:
            print("The part of the email after the '@' is too long (max. 189 characters)")
            print(f"DEBUG: Domain's length = {len(domain)}")
            continue

        # Validate format with regex
        if not re.fullmatch(pattern, email):
            print("Invalid email format")
            continue

        print("✅ Email accepted")
        return email
    # ---------------------------


def get_town_postcode():
    """
    Validates the town and postcode with the following rules:
      - Town: one or more words consisting only of letters (accents and the letter Ñ are allowed).
      - Postcode: exactly 4 digits, which must appear at the end, separated from the town by at least one space.

    Returns:
        str: Combined string "Town Postcode" (for example, "Graz 8045").
    """
    import re
    # Regex pattern:
    # ^                                  : start of the string
    # ([A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+)*)
    #     -> group 1, town name consisting of one or more words
    # \s+                                : at least one space
    # (\d{4})                            : group 2, exactly 4 digits for the postcode
    # $                                  : end of the string
    pattern = re.compile(r"^([A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+)*)\s+(\d{4})$")

    error_found = True

    while error_found == True:
        town_postcode = input("Give the town and postcode (e.g., 'Graz 8045'): ")
        town_postcode = clean_input(town_postcode)
        town_list = town_postcode.split()

        if pattern.fullmatch(town_postcode):
            error_found = False
        else:
            print("Error: Enter town and postcode in the correct format (e.g., 'Graz 8045').")

        return town_postcode
# ---------------------------


#   format user data into comma separated string
def combined_data(name, phone, birth_date, address_street, address_town, email):
    """
        Combines user data into a CSV-style string.

        Args:
            All individual user data fields.

        Returns:
            str: Comma-separated data string.
        """
    all_data = f"{name},{phone},{birth_date},{address_street},{address_town},{email}"

    return all_data

#   get all the data fields, put into formatted string, and return that string
def get_user_data ():
    """
        Orchestrates data collection by calling all validation functions.

        Returns:
            str: Combined data string for one user.
        """
    name = get_name()
    phone = get_phone()
    birth_date = get_birth_date()
    address_street = get_address_street()
    address_town = get_town_postcode()
    email = get_email()

    #  combine data into a string and place into list
    all_data = combined_data(name, phone, birth_date, address_street, address_town, email)

    return all_data
# ---------------------------


# add a new user to the database
def register_data_function(file_path):
    """
        Registers a new user by:
        1. Collecting validated data
        2. Appending to the file
        """
    print("Please enter the employee or visitor information")

    one_user_data= get_user_data()  # retrieve formatted user data

    # Final confirmation based on validation
    print("\nUser successfully entered into the database.")
    name = one_user_data[0]
    address_street = one_user_data[1]
    address_town = one_user_data[2]
    birth_date = one_user_data[3]
    phone = one_user_data[4]
    email = one_user_data[5]

    print_users_data(name, address_street, address_town, birth_date, phone, email)  # print user data

    with open(file_path, "a") as user_file:    # append user to database
        user_file.write(one_user_data + "\n")

 # read in user data and return as a list of strings

def read_users_into_list (file_path):
    """
        Reads all users from file into a list.

        Returns:
            list: Each element is a line from the file.
        """
    with open(file_path, "r") as user_file:  # Opens the file located in file_path in reading mode ("r")
        users_list = [line.strip() for line in user_file]

    return users_list
# ---------------------------


def search_data_function(file_path):
    """
       Searches for users by name (case-insensitive substring match).
       Returns nothing; prints match or "no match" to screen.
       """
    users_list = read_users_into_list(file_path)


    search_for_keyword = input("Which name are you looking for?: ").strip().lower()

    found_keyword = False

    for user in users_list:                               # loop until user found or list is finished
        individual_user_list = user.split(",")
        name = individual_user_list[0]
        name = name.lower()
        address_street = individual_user_list[1]
        address_town = individual_user_list[2]
        birth_date = individual_user_list[3]
        phone = individual_user_list[4]
        email = individual_user_list[5]

        if search_for_keyword in name:
            found_keyword = True
            print_users_data(name, address_street, address_town, birth_date, phone, email)

    if found_keyword == False:
        print("\nNo matches :(")


# Function to allow the user to modify data

def modify_data_function(file_path):
    """
        Modifies an existing user's record by:
        1. Finding the user
        2. Collecting new data
        3. Rewriting the entire file
        """
    users_list = read_users_into_list(file_path)


    user_name = input("Which name do you want to change?: ")
    user_name = user_name.lower()

    found = -1

    for pos, user_data in enumerate (users_list):

        if user_name in user_data:
            found = pos
            break

    if found == -1:
        print("Sorry, not found.")

    else:
        print("Super! Found it!")
        one_user_data = get_user_data()
        # print(one_user_data)  # For debug purposes
        users_list[pos] = one_user_data
        print(users_list)

        with open(file_path, "w") as user_file:
            for element in users_list:
                user_file.write(element + "\n")



# ---------------------- MAIN PROGRAM ----------------------

file_path = "C:/Users/Lily/Documents/Personal files/Fohnsdorf School/Qualifizierung/Python/user_register.txt"
users_list = []


while True:
    print("\nWhat would you like to do?")
    print("1. Register users")
    print("2. Search for data") # print data print filtered data
    print("3. Modify data")
    print("4. Quit program")

    choose_option = input("Choose an option (1, 2, 3, 4): ")

    if choose_option == "1":
        print("You chose the option: Register users")
        register_data_function(file_path)

    elif choose_option == "2":
        print("You chose the option: Search for data")
        search_data_function(file_path)

    elif choose_option == "3":
        print("You chose: Modify data")
        modify_data_function(file_path)

    elif choose_option == "4":
        break

# print goodbye message, write out user data, and exit program
print("Exiting the system. Goodbye!")


