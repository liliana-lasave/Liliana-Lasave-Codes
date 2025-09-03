public class Animal {
    private String name;
    private int age;

    // Constructor
    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    // Method to overwrite in the subclasses
    public String makeSound() {
        return "I can make sound.";
    }


    // To store data in CSV: "name, age". It converts the object information in a CSV row
    public String toCsvRow() {
        return name + "," + age;

    }

}
