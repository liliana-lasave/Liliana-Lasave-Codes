public class MotorcycleClass extends VehicleClass {
    private String color;
    private static int numberOfMotorcycles = 0;

    public MotorcycleClass(String modelIn, int yearIn, String colorIn) {
        super(modelIn, yearIn);
        this.color = (colorIn == null || colorIn.trim().isEmpty())
                ? "UNKNOWN" : colorIn.trim();
        numberOfMotorcycles++;
    }

    @Override
    public String type() { return "MOTORCYCLE"; }

    // TYPE,MODEL,YEAR,FUEL,MILEAGE,EXTRA1,EXTRA2
    @Override
    public String toCsvRow() {
        return type() + "," + getModel() + "," + getYear() + ","
                + getFuelAmount() + "," + getMileage() + ","
                + color + ",";
    }

    public String getColor() { return color; }
    public void setColor(String color) {
        this.color = (color == null || color.trim().isEmpty())
                ? "UNKNOWN" : color.trim();
    }

    public static int getNumberOfMotorcycles() { return numberOfMotorcycles; }

    public void showVehicleInfo() {
        System.out.println("I have a " + getYear() + " " + getModel() + " motorcycle.");
    }

    @Override
    public String toString() {
        return "MotorcycleClass{" +
                "model='" + getModel() + '\'' +
                ", year=" + getYear() +
                ", fuelAmount=" + getFuelAmount() +
                ", mileage=" + getMileage() +
                ", color='" + color + '\'' +
                '}';
    }
}
