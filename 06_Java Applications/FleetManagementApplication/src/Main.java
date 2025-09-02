import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String file = "vehicles.csv";

        // 1) Build a polymorphic list (base type holds all subtypes)
        List<VehicleClass> vehicles = new ArrayList<>();
        vehicles.add(new CarClass("Steamer", 1949, "water", 80));
        vehicles.add(new CarClass("HydroCar", 2026, "H2", 140));
        vehicles.add(new TruckClass("FleetGiant", 2005, "10 Ton"));
        vehicles.add(new MotorcycleClass("Ninja", 2020, "Green"));
        vehicles.add(new BicycleClass("XC-Pro", 2022, "Carbon", "MTB"));

        // 2) SAVE to CSV (overwrites the file each run)
        CsvUtilVehicles.save(file, vehicles);
        System.out.println("CSV saved to: " + file);

        // 3) READ CSV as rows (simple): TYPE,MODEL,YEAR,FUEL,MILEAGE,EXTRA1,EXTRA2
        List<String[]> rows = CsvUtilVehicles.readRows(file);
        System.out.println("CSV content:");
        for (String[] r : rows) {
            // Guard against short lines
            String type = r.length > 0 ? r[0] : "";
            String model = r.length > 1 ? r[1] : "";
            String year = r.length > 2 ? r[2] : "";
            String fuel = r.length > 3 ? r[3] : "";
            String km   = r.length > 4 ? r[4] : "";
            String extra1 = r.length > 5 ? r[5] : "";
            String extra2 = r.length > 6 ? r[6] : "";
            System.out.println("- " + type + " | " + model + " | year=" + year +
                    " | fuel=" + fuel + " | km=" + km + " | " + extra1 + " " + extra2);
        }
    }
}
