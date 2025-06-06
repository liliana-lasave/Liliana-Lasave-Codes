import sys
import os

# Add project root to sys.path for proper imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from products.products_liliwelt import PrivateLesson, GroupWorkshop, Course
from products.storage_liliwelt import Storage

# Initialize database and create tables
storage = Storage("liliwelt.db")
storage.create_tables()

# --- Create and save PrivateLesson ---
lesson = PrivateLesson(
    name="Basic Piano",
    price=50.0,
    duration="4 weeks",
    level="Beginner",
    audience="Children",
    modality="In-person",
    teacher_name="Prof. Ana",
    instrument="Piano"
)
storage.save_product(lesson)
print(f"✅ PrivateLesson ID: {lesson.id}")
assert lesson.id is not None and isinstance(lesson.id, int)

# --- Create and save GroupWorkshop ---
workshop = GroupWorkshop(
    name="Tango Rhythms",
    price=80.0,
    duration="1 day",
    level="Intermediate",
    audience="Adults",
    modality="Online",
    theme="Argentinian Tango",
    max_participants=12
)
storage.save_product(workshop)
print(f"✅ GroupWorkshop ID: {workshop.id}")
assert workshop.id is not None and isinstance(workshop.id, int)

# --- Create and save Course ---
course = Course(
    name="Advanced Vocal Training",
    price=120.0,
    duration="8 weeks",
    level="Advanced",
    audience="Adults",
    modality="In-person",
    num_sessions=16,
    certificate=True
)
storage.save_product(course)
print(f"✅ Course ID: {course.id}")
assert course.id is not None and isinstance(course.id, int)

# --- Load and display all products ---
print("\n📦 Loaded products from the database:")
all_products = storage.load_all_products()
for product in all_products:
    print("-", product.get_info())

print("\n🎉 All products saved and loaded successfully!")
