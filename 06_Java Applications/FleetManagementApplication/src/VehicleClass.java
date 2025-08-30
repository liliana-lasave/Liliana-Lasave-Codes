public class VehicleClass {
    String model;
    int year;
    int fuelAmount = 0;// Bicycles will not use fuel, but the other 3 they will.
    int mileage = 0;
    static int numberOfVehicles = 0;

    // Constructor that is counting vehicles, called when I create any child object


     public VehicleClass(String modelIn, int yearIn) {
            this.model = modelIn;
            this.year = yearIn;
            numberOfVehicles++;
        }

    // Setter to add fuel to the vehicles
    public void addFuel (int newFuelAmount) {       // newFuelAmount → is the number entered as a parameter or temporary variable (the amount of fuel I want to add).
        fuelAmount = fuelAmount + newFuelAmount;    // Update the fuelAmount attribute by adding the newFuelAmount amount I received.
    }

    // Getter to get the amount of fuel
    public int getFuelAmount() {
        return fuelAmount;
    }

    // Setter to add km travelled to the vehicles
    public void addKm (int newKmNumber) {
        mileage = mileage + newKmNumber;    // Update the fuelAmount attribute by adding the newFuelAmount amount I received.
    }

    // Getter to get the number of km travelled
    public int getMileage() {
        return mileage;
    }

}

