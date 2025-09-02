public class VehicleClass {
    // Fields (encapsulation)
    private String model;
    private int year;
    private int fuelAmount = 0; // Bicycles will not use fuel, but the other 3 will.
    private int mileage = 0;
    private static int numberOfVehicles = 0;

    // Constructor that counts vehicles; called when I create any child object
    public VehicleClass(String modelIn, int yearIn) {
        this.model = modelIn;
        this.year = yearIn;
        numberOfVehicles++;
    }

    // Setter to add fuel to the vehicles
    public void addFuel(int newFuelAmount) {
        if (newFuelAmount < 0) return;    // simple guard
        fuelAmount += newFuelAmount;
    }

    // Setter to add km travelled to the vehicles
    public void addKm(int newKmNumber) {
        if (newKmNumber < 0) return;      // simple guard
        mileage += newKmNumber;
    }

    // Getters / Setters
    public String getModel() { return model; }
    public void setModel(String model) { this.model = model; }

    public int getYear() { return year; }
    public void setYear(int year) {
        if (year < 1886) return;          // first car ~1886; keep it simple
        this.year = year;
    }

    public int getFuelAmount() { return fuelAmount; }
    public void setFuelAmount(int fuelAmount) {
        if (fuelAmount < 0) return;
        this.fuelAmount = fuelAmount;
    }

    public int getMileage() { return mileage; }
    public void setMileage(int mileage) {
        if (mileage < 0) return;
        this.mileage = mileage;
    }

    public static int getNumberOfVehicles() { return numberOfVehicles; }

    @Override
    public String toString() {
        return "VehicleClass{" +
                "model='" + model + '\'' +
                ", year=" + year +
                ", fuelAmount=" + fuelAmount +
                ", mileage=" + mileage +
                '}';
    }

    // Polymorphic label for CSV type
    public String type() { return "VEHICLE"; }

    // CSV header compatible with all subtypes (two generic extras)
    public static String csvHeader() {
        return "TYPE,MODEL,YEAR,FUEL,MILEAGE,EXTRA1,EXTRA2";
    }

    // CSV row for the base class (extras left empty)
    public String toCsvRow() {
        return String.join(",",
                type(),
                String.valueOf(getModel()),
                String.valueOf(getYear()),
                String.valueOf(getFuelAmount()),
                String.valueOf(getMileage()),
                "", // EXTRA1
                ""  // EXTRA2
        );
    }
}
