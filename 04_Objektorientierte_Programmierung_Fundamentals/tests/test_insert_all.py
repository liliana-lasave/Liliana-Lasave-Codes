# Import the Storage class and product classes
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'products')))
from storage_liliwelt import Storage
from products.products_liliwelt import PrivateLesson, GroupWorkshop, Course

# Create the data connection using the correct relative path
storage = Storage(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'liliwelt.db')))
storage.create_tables()

# --------- PrivateLesson ----------
lesson = PrivateLesson(
    name="Beginner Piano",
    price=30.0,
    duration="45min",
    level="beginner",
    audience="children",
    modality="in-person",
    teacher_name="Lili",
    instrument="piano"
)
storage.save_product(lesson)

# --------- GroupWorkshop ----------
workshop = GroupWorkshop(
    name="Latin Rhythms Workshop",
    price=40.0,
    duration="1h",
    level="intermediate",
    audience="adults",
    modality="online",
    theme="Tango & Samba",
    max_participants=12
)
storage.save_product(workshop)

# --------- Course ----------
course = Course(
    name="Full Voice Course",
    price=200.0,
    duration="10 weeks",
    level="advanced",
    audience="mixed",
    modality="hybrid",
    num_sessions=10,
    certificate=True
)
storage.save_product(course)

print("All products saved successfully!")

