public class BicycleClass extends VehicleClass {
    String model;
    int year;
    int fuelAmount = 0;
    int mileage = 0;
    String material;      // Attribute of the class BicycleClass
    String type;
    static int numberOfBicycles = 0;    // static because it is a class variable



    // Constructor
    public BicycleClass(String modelIn, int yearIn, String materialIn, String typeIn) {     // ("temporary variables that only belong to the constructor")
        super(modelIn, yearIn);
        //this.model = modelIn;
        //this.year = yearIn;
        this.material = materialIn;
        this.type = typeIn;
        numberOfBicycles++;
    }

    // Override the method addFuel inherited from the parent class VehicleClass
    @Override  public void addFuel (int newFuelAmount) {       // newFuelAmount → is the number entered as a parameter or temporary variable (the amount of fuel I want to add).
        System.out.println("Our bicycles do not need any fuel, since they are human powered.");    // Update the fuelAmount attribute by adding the newFuelAmount amount I received.
    }

    // Getter for BicycleClass
    public String getModel() {
        return model;
    }

    // Getter for BicycleClass
    public int getYear() {
        return year;
    }

    // Method to see info of the bicycle
    public void showVehicleInfo() {
        System.out.println("I have a "+ type + "-" + model + " bicycle" + " made out of " + material +".");
    }




}

