// Dog: EXTRA1 = breed, EXTRA2 = foodType

public class Dog extends Animal {
    private String breed;           // EXTRA1
    private String foodType;        // EXTRA2


    // Constructor
    public Dog(int id, String name, int age, String breed, String foodType) {
        super(id, name, age);
        this.breed = safe(breed);
        this.foodType = safe(foodType);
    }

    // Getters and Setters
    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = safe(breed);
    }

    public String getFoodType() {
        return foodType;
    }

    public void setFoodType(String foodType) {
        this.foodType = safe(foodType);
    }

    // Polymorphic label
    @Override
    public String type() {
        return "DOG";
    }

    // CSV extras (two optional fields)
    @Override
    public String[] extrasForCsv() {
        return new String[]{breed, foodType};           // String[], without size
    }

}
