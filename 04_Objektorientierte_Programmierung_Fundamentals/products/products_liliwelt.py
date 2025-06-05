from abc import ABC, abstractmethod         # Import abstract base classes and decorators to create abstract methods

# Define an abstract base class for all products
class Product(ABC):
    _id_counter = 1                         # Class variable to auto-increment and assign unique IDs to each product instance

    def __init__(self, name, price, duration, level, audience, modality):

        # Assign a unique ID to the product and increment the counter
        self.id = Product._id_counter
        Product._id_counter += 1

        # Set the product's basic attributes
        self.name = name                    # Product name (class title)
        self.price = price                  # Product price (in euros)
        self.duration = duration            # Product duration (number of weeks or hours)
        self.level = level                  # Difficulty level (beginner, intermediate, advanced)
        self.audience = audience            # Target audience (kids, adults)
        self.modality = modality            # Modality (online, in-person)
        self.ratings = []                   # List to store user ratings (1 to 5 stars)

    # Add a rating to the product if it's between 1 and 5 stars
    def add_rating(self, stars):
        if 1 <= stars <= 5:
            self.ratings.append(stars)

    # Calculate and return the average rating, or None if there are no ratings
    def average_rating(self):
        if not self.ratings:
            return None
        return sum(self.ratings) / len(self.ratings)

    # Abstract method that must be implemented by all subclasses
    @abstractmethod
    def get_info(self):
        pass


# Subclass for private lessons
class PrivateLesson(Product):
    def __init__(self, name, price, duration, level, audience, modality, teacher_name, instrument):
        super().__init__(name, price, duration, level, audience, modality)

        self.teacher_name = teacher_name  # Name of the teacher
        self.instrument = instrument  # Instrument (e.g., voice, piano)

    def get_info(self):
        return f"Private lesson with {self.teacher_name} on {self.instrument} ({self.level}) for {self.audience}, {self.duration}, {self.price}€ [{self.modality}]"

# Subclass for group workshops
class GroupWorkshop(Product):
    def __init__(self, name, price, duration, level, audience, modality, theme, max_participants):
        super().__init__(name, price, duration, level, audience, modality)

        self.theme = theme  # Theme of the workshop
        self.max_participants = max_participants  # Maximum number of participants

    def get_info(self):
        return f"Group workshop on '{self.theme}' ({self.level}) for up to {self.max_participants} {self.audience}, {self.duration}, {self.price}€ [{self.modality}]"

# Subclass for multi-session courses
class Course(Product):
    def __init__(self, name, price, duration, level, audience, modality, num_sessions, certificate):
        super().__init__(name, price, duration, level, audience, modality)

        self.num_sessions = num_sessions  # Number of sessions
        self.certificate = certificate  # Whether it includes a certificate

    def get_info(self):
        cert_text = "with certificate" if self.certificate else "no certificate"
        return f"Course ({self.level}) for {self.audience}, {self.num_sessions} sessions over {self.duration}, {self.price}€ [{self.modality}, {cert_text}]"

