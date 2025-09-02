public class TruckClass extends VehicleClass {
    private String cargoType;          // e.g., "10 Ton"
    private static int numberOfTrucks = 0;

    public TruckClass(String modelIn, int yearIn, String cargoTypeIn) {
        super(modelIn, yearIn);
        this.cargoType = (cargoTypeIn == null || cargoTypeIn.trim().isEmpty())
                ? "UNKNOWN" : cargoTypeIn.trim();
        numberOfTrucks++;
    }

    @Override
    public String type() { return "TRUCK"; }

    // TYPE,MODEL,YEAR,FUEL,MILEAGE,EXTRA1,EXTRA2
    @Override
    public String toCsvRow() {
        return type() + "," + getModel() + "," + getYear() + ","
                + getFuelAmount() + "," + getMileage() + ","
                + cargoType + ",";
    }

    public String getCargoType() { return cargoType; }
    public void setCargoType(String cargoType) {
        this.cargoType = (cargoType == null || cargoType.trim().isEmpty())
                ? "UNKNOWN" : cargoType.trim();
    }

    public static int getNumberOfTrucks() { return numberOfTrucks; }

    public void showVehicleInfo() {
        System.out.println("I have a " + getModel() + " truck with a capacity of " + cargoType + ".");
    }

    @Override
    public String toString() {
        return "TruckClass{" +
                "model='" + getModel() + '\'' +
                ", year=" + getYear() +
                ", fuelAmount=" + getFuelAmount() +
                ", mileage=" + getMileage() +
                ", cargoType='" + cargoType + '\'' +
                '}';
    }
}
