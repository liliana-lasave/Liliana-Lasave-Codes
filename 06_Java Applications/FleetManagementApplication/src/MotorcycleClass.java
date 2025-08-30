public class MotorcycleClass extends VehicleClass {
    String model;
    int year;
    int fuelAmount = 0;
    int mileage = 0;
    int speed;      // Attribute of the class MotorcycleClass
    String color;
    static int numberOfMotorcycles = 0;    // static because it is a class variable


// Constructor
public MotorcycleClass(String modelIn, int yearIn, int speedIn, String colorIn) {     // ("temporary variables that only belong to the constructor")
    super(modelIn, yearIn);
    //this.model = modelIn;
    //this.year = yearIn;
    this.speed = speedIn;
    this.color = colorIn;
    numberOfMotorcycles++;
}

// Getter for MotorcycleClass
public String getModel() {
    return model;
}

// Getter for MotorcycleClass
public int getYear() {
    return year;
}

// Method to see info of the motorcycle
public void showVehicleInfo() {
    System.out.println("I have a "+ model +" motorcycle"+" from " + year +".");
}

}

