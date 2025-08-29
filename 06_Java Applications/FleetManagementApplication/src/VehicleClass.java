public class VehicleClass {
    String model;
    int year;
    int fuelAmount = 0;     // Bicycles will not use fuel, but the other 3 they will.
    static int numberOfVehicles = 0;

    // Constructor that is counting vehicles, called when I create an object
    VehicleClass() {
        numberOfVehicles++;

    }

    // Setter to add fuel to the vehicles
    public void addFuel (int newFuelAmount) {
        fuelAmount = fuelAmount + newFuelAmount;
    }

    // Getter to get the amount of fuel
    public int getFuelAmount() {
        return fuelAmount;
    }
}

