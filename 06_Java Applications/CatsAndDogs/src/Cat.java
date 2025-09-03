public class Cat extends Animal {
    private String origin;      // if it is wild or domesticated

    public String getOrigin() {
        return origin;
    }

    public Cat(String name, int age, String origin) {
        super(name, age);
        this.origin = origin;
    }

    public void setOrigin(String origin) {
        this.origin = origin;
    }

    @Override
    public String makeSound() {
        return "Miau!";
    }

    public void printInfo() {
        System.out.println("The cat´s name is " + getName() + ", it is " + getAge() + " years old and it is " + this.origin + ". It makes " + makeSound());}

    @Override
    public String toCsvRow() {
        return "cat," + super.toCsvRow() + "," + getOrigin();
    }
}
