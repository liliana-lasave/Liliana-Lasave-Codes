
"""A static method (@staticmethod) is a method that belongs to a class but
does not access or modify instance attributes (self) or class attributes (cls).
It is ideal for auxiliary functions such as validation, which do not depend on the state of the object.
 """

from datetime import datetime


class Validator:
# -------------------
# Check if the email address has a valid format.
# -------------------

    @staticmethod
    def validate_email (email):
        if email.count("@") != 1:
            return False
        if len(email) > 255:
            return False
        if " " in email:
            return False
        before, after = email.split("@")
        if len(before) > 64 or len(after) == 0:
            return False
        if "." not in after:
            return False
        if before.startswith(".") or before.endswith("."):
            return False
        if ".." in before:
            return False
        if ".." in after:
            return False
        if after.startswith(".") or after.endswith("."):
            return False
        if len(before) == 0:
            return False
        tld = after.split(".")[-1]
        if len(tld) < 2:
            return False
        return True


    # -------------------
    # Validate the phone number. Must de 8-20 characters, digits, optional + or 00 prefix.
    # -------------------

    @staticmethod
    def validate_phone(phone):
        phone = phone.strip()
        if " " in phone:
            return False
        if len(phone.strip()) == 0:
            return False
        if len(phone) < 8 or len(phone) >20:
            return False
        if phone.startswith("+"):
            if not phone[1:].isdigit():
                return False
        elif phone.startswith("00"):
            if not phone[2:].isdigit():
                return False
        else:
            if not phone.isdigit():
                return False

        return True


    # -------------------
    # Validate a personal name (letters, spaces, hyphens and apostrophes allowed).
    # -------------------

    @staticmethod

    def validate_name(name):
        name = name.strip()
        if len(name) == 0:
            return False
        for char in name:
            if not (char.isalpha() or char in " -'."):
                return False
        return True


    # -------------------
    # Validate an address (letters, digits, common punctuation).
    # -------------------

    @staticmethod
    def validate_address(address):
        address = address.strip()
        if len(address) == 0:
            return False
        for char in address:
            if not (char.isalpha() or char.isdigit() or char in " -°'/.,"):
                return False
        return True


    # -------------------
    # Validate a postcode (digits only, length between 4 and 10).
    # -------------------

    @staticmethod
    def validate_postcode(postcode):
        postcode = postcode.strip()
        if len(postcode) == 0:
            return False
        if not postcode.isdigit():
            return False
        if len(postcode) < 4 or len(postcode) > 10:
            return False
        return True


    # -------------------
    # Validate locality name (letters, spaces, hyphens and apostrophes allowed).
    # -------------------

    @staticmethod
    def validate_locality(locality):
        locality = locality.strip()
        if len(locality) == 0:
            return False
        for char in locality:
            if not (char.isalpha() or char in " -'"):
                return False
        return True



    # -------------------
    # Validate birthdate format (DD.MM.YYYY) and ensure it is not in the future.
    # -------------------

    @staticmethod
    def validate_birthdate(birthdate):
        try:
            date = datetime.strptime(birthdate, "%d.%m.%Y")
            if date > datetime.now():
                return False
            return True
        except ValueError:
            return False



    # -------------------
    # Validate company number (digits only, length between 5 and 15).
    # -------------------

    @staticmethod
    def validate_company_number(cn):
        cn = cn.strip()
        if len(cn) == 0:
            return False
        if not cn.isdigit():
            return False
        if not (5 <= len(cn) <= 15):
            return False
        return True



    # -------------------
    # Validate password (at least 6 characters, not empty).
    # -------------------

    @staticmethod
    def validate_password(password):
        if not isinstance(password, str):
            return False
        if len(password.strip()) < 6:
            return False

        return True
