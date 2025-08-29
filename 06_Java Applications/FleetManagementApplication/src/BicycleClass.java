public class BicycleClass extends VehicleClass {
    String material;      // Attribute of the class BicycleClass
    String type;
    static int numberOfBicycles = 0;    // static because it is a class variable


    // Constructor
    public BicycleClass(String modelIn, int yearIn, String materialIn, String typeIn) {     // ("temporary variables that only belong to the constructor")
        this.model = modelIn;
        this.year = yearIn;
        this.material = materialIn;
        this.type = typeIn;
        numberOfBicycles++;
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

