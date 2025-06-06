from customers.customer_liliwelt import Customer
from validation.validator_liliwelt import Validator
from datetime import datetime


class Private_customer(Customer):
    def __init__(self, name, address, postcode, locality, email, phone, password, birthdate):

        super().__init__(name, address, postcode, locality, email, phone, password)

        if not Validator.validate_birthdate(birthdate):
            raise ValueError("Invalid birthdate")

        self.birthdate = birthdate

    def get_birthdate(self):

        return self.birthdate

    def get_age(self):

        birthdate_edited = datetime.strptime(self.birthdate, "%d.%m.%Y")   # Convertion from string to datetime object.
        today = datetime.today()
        age = today.year - birthdate_edited.year

        if (today.month, today.day) < (birthdate_edited.month, birthdate_edited.day):
            age -= 1

        return age
