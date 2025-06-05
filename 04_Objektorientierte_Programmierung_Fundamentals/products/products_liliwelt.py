from abc import ABC, abstractmethod


class Product(ABC):
    _id_counter = 1

    def __init__(self, name, price, duration, level, audience, modality):
        self.id = Product._id_counter
        Product._id_counter += 1
        self.name = name
        self.price = price
        self.duration = duration
        self.level = level
        self.audience = audience
        self.modality = modality
        self.ratings = []

    def add_rating(self, stars):
        if 1 <= stars <= 5:
            self.ratings.append(stars)

    def average_rating(self):
        if not self.ratings:
            return None
        return sum(self.ratings) / len(self.ratings)

    @abstractmethod
    def get_info(self):
        pass