public class TruckClass extends VehicleClass {
    String model;
    int year;
    int fuelAmount = 0;
    int mileage = 0;
    String cargoType;      // Attribute of the class Truck
    static int numberOfTrucks = 0;  // static because it is a class variable

    // Constructor
    public TruckClass(String modelIn, int yearIn, String cargoTypeIn) {     // ("temporary variables that only belong to the constructor")
        super(modelIn, yearIn);
        //this.model = modelIn;
        //this.year = yearIn;
        this.cargoType = cargoTypeIn;
        numberOfTrucks++;

        }

    // Getter for CarClass
    public String getModel() {
        return model;
        }

    // Getter for TruckClass
    public String getcargoType() {
        return cargoType;
    }

    // Method to see info of the truck
    public void showVehicleInfo() {
        System.out.println("I have a "+ model +" truck"+" with a maximum capacity of " + cargoType +" Tons.");
    }

}



