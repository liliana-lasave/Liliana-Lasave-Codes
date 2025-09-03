public class Dog extends Animal {
    private String foodType;

    public Dog(String name, int age, String foodType) {     // Constructor that receives name, age and type of food
        super(name, age);                                   // Call the constructor of the base class in order that Animal stores name and age.
        this.foodType = foodType;                           // stores the value that is passed by parameter in the attribute of the Dog foodType
    }

    public String getFoodType() {
        return foodType;
    }

    public void setFoodType(String foodType) {
        this.foodType = foodType;
    }

    @Override
    public String makeSound() {
        return "Woof!";
    }

    public void printInfo() {
        System.out.println("The dog´s name is " + getName() + ", it is " + getAge() + " years old and its favourite food is " + this.foodType + ". It makes " + makeSound());
    }

    @Override
    public String toCsvRow() {
        return "dog," + super.toCsvRow() + "," + getFoodType();
    }
}
