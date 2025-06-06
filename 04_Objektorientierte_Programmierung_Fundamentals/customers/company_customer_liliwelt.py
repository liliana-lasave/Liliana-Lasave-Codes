from customers.customer_liliwelt import Customer
from validation.validator_liliwelt import Validator

class Company_customer(Customer):

    def __init__(self, name, address, postcode, locality, email, phone, password, company_number):
        super().__init__(name, address, postcode, locality, email, phone, password)

        if not Validator.validate_company_number(company_number):
            raise ValueError("Invalid company number")

        self.company_number = company_number

    def get_company_number(self):
        return self.company_number

    def set_company_number(self, company_number):
        if not Validator.validate_company_number(company_number):
            raise ValueError("Invalid company number")

        self.company_number = company_number
