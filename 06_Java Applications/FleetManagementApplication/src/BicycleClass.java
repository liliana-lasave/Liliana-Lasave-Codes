public class BicycleClass extends VehicleClass {
    private String material;   // e.g., "Carbon", "Aluminum"
    private String bykeType;       // e.g., "MTB", "Road"
    private static int numberOfBicycles = 0;

    public BicycleClass(String modelIn, int yearIn, String materialIn, String typeIn) {
        super(modelIn, yearIn);
        this.material = (materialIn == null || materialIn.trim().isEmpty())
                ? "UNKNOWN" : materialIn.trim();
        this.bykeType = (typeIn == null || typeIn.trim().isEmpty())
                ? "UNKNOWN" : typeIn.trim();
        numberOfBicycles++;
    }

    @Override
    public String type() { return "BICYCLE"; }

    // TYPE,MODEL,YEAR,FUEL,MILEAGE,EXTRA1,EXTRA2
    @Override
    public String toCsvRow() {
        return type() + "," + getModel() + "," + getYear() + ","
                + getFuelAmount() + "," + getMileage() + ","
                + material + "," + this.bykeType;
    }

    public String getMaterial() { return material; }
    public void setMaterial(String material) {
        this.material = (material == null || material.trim().isEmpty())
                ? "UNKNOWN" : material.trim();
    }

    public String getBikeType() { return this.bykeType; }
    public void setBikeType(String type) {
        this.bykeType = (type == null || type.trim().isEmpty())
                ? "UNKNOWN" : type.trim();
    }

    public static int getNumberOfBicycles() { return numberOfBicycles; }

    public void showVehicleInfo() {
        System.out.println("I have a " + this.bykeType + "-" + getModel() + " bicycle made of " + material + ".");
    }

    @Override
    public String toString() {
        return "BicycleClass{" +
                "model='" + getModel() + '\'' +
                ", year=" + getYear() +
                ", fuelAmount=" + getFuelAmount() +
                ", mileage=" + getMileage() +
                ", material='" + material + '\'' +
                ", type='" + this.bykeType + '\'' +
                '}';
    }

    @Override
    public void addFuel(int newFuelAmount) {
        System.out.println("Our bicycles do not need any fuel, since they are human powered.");
    }
}
