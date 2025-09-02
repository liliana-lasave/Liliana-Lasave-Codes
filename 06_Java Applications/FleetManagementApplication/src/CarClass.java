public class CarClass extends VehicleClass {
    // Car fields
    private String engineType;
    private int speed;
    private static int numberOfCars = 0;

    // Constructor (simple checks)
    public CarClass(String modelIn, int yearIn, String engineTypeIn, int speedIn) {
        super(modelIn, yearIn);
        this.engineType = (engineTypeIn == null || engineTypeIn.trim().isEmpty())
                ? "UNKNOWN" : engineTypeIn.trim();
        this.speed = Math.max(0, speedIn); // no negative speed
        numberOfCars++;
    }

    @Override
    public String type() { return "CAR"; }

    // CSV row (TYPE,MODEL,YEAR,FUEL,MILEAGE,EXTRA1,EXTRA2)
    @Override
    public String toCsvRow() {
        return type() + "," + getModel() + "," + getYear() + ","
                + getFuelAmount() + "," + getMileage() + ","
                + engineType + "," + speed;
    }

    // Getters / setters (simple validation)
    public String getEngineType() { return engineType; }
    public void setEngineType(String engineType) {
        this.engineType = (engineType == null || engineType.trim().isEmpty())
                ? "UNKNOWN" : engineType.trim();
    }

    public int getSpeed() { return speed; }
    public void setSpeed(int speed) { this.speed = Math.max(0, speed); }

    public static int getNumberOfCars() { return numberOfCars; }

    // Optional
    public void showVehicleInfo() {
        System.out.println("I have a " + getModel() + " car powered by " + engineType + ".");
    }

    @Override
    public String toString() {
        return "CarClass{" +
                "model='" + getModel() + '\'' +
                ", year=" + getYear() +
                ", fuelAmount=" + getFuelAmount() +
                ", mileage=" + getMileage() +
                ", engineType='" + engineType + '\'' +
                ", speed=" + speed +
                '}';
    }
}
