public class CarClass extends VehicleClass {
    String model;
    int year;
    int fuelAmount = 0;
    int mileage = 0;
    String engineType;      // Attribute of the class CarClass
    static int numberOfCars = 0;    // static because it is a class variable


    // Constructor
    public CarClass(String modelIn, int yearIn, String engineTypeIn) {     // ("temporary variables that only belong to the constructor")
        super(modelIn, yearIn);
        //this.model = modelIn;
        //this.year = yearIn;
        this.engineType = engineTypeIn;
        numberOfCars++;


    }

    // Getter for CarClass
    public String getModel() {
        return model;
    }

    // Getter for CarClass
    public String getEngineType() {
        return engineType;
    }

    // Method to see all the info of the car
    public void showVehicleInfo() {
        System.out.println("I have a "+ model +" car"+" powered by " + engineType +".");
    }

}

