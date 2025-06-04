from validator_liliwelt import Validator

class Customer:
    _id_counter = 1 # class variable to auto-generate unique IDs

    def __init__(self, name, address, postcode, locality, email, phone, password):
        self.id = Customer._id_counter
        Customer._id_counter += 1

        if not Validator.validate_name(name):
            raise ValueError("Invalid name")
        if not Validator.validate_address(address):
            raise ValueError("Invalid address")
        if not Validator.validate_postcode(postcode):
            raise ValueError("Invalid postcode")
        if not Validator.validate_locality(locality):
            raise ValueError("Invalid locality")
        if not Validator.validate_email(email):
            raise ValueError("Invalid email")
        if not Validator.validate_phone(phone):
            raise ValueError("Invalid phone")
        if not Validator.validate_password(password):
            raise ValueError("Invalid password")

        self.name = name
        self.address = address
        self.postcode = postcode
        self.locality = locality
        self.email = email
        self.phone = phone
        self.password = password

    def get_id(self):
        return self.id


    def get_name(self):
        return self.name

    def set_name(self, name):
        if not Validator.validate_name(name):
            raise ValueError("Invalid name")
        self.name = name


    def get_address(self):
        return self.address

    def set_address(self, address):
        if not Validator.validate_address(address):
            raise ValueError("Invalid address")
        self.address = address


    def get_postcode(self):
        return self.postcode

    def set_postcode(self, postcode):
        if not Validator.validate_postcode(postcode):
            raise ValueError("Invalid postcode")
        self.postcode = postcode


    def get_locality(self):
        return self.locality

    def set_locality(self, locality):
        if not Validator.validate_locality(locality):
            raise ValueError("Invalid locality")
        self.locality = locality


    def get_email(self):
        return self.email

    def set_email(self, email):
        if not Validator.validate_email(email):
            raise ValueError("Invalid email")
        self.email = email


    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        if not Validator.validate_phone(phone):
            raise ValueError("Invalid phone")
        self.phone = phone


    def get_password(self):
        return self.password

    def set_password(self, password):
        if not Validator.validate_password(password):
            raise ValueError("Invalid password")
        self.password = password


