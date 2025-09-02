import java.io.*;
import java.util.ArrayList;
import java.util.List;

/** Super-simple CSV utility: save/append vehicles and read raw rows. */
public final class CsvUtilVehicles {
    private CsvUtilVehicles() {}

    /** Overwrite file with header + all vehicle rows (optional, keep for resets). */
    public static void save(String path, List<? extends VehicleClass> vehicles) {
        try (PrintWriter out = new PrintWriter(new FileWriter(path))) {
            out.println(VehicleClass.csvHeader());        // header
            for (VehicleClass v : vehicles) out.println(v.toCsvRow());
        } catch (IOException e) {
            System.out.println("Error writing CSV: " + e.getMessage());
        }
    }

    /** Append rows to CSV. Writes header only if file doesn't exist or is empty. */
    public static void append(String path, List<? extends VehicleClass> vehicles) {
        File f = new File(path);
        boolean writeHeader = !f.exists() || f.length() == 0L;

        try (FileWriter fw = new FileWriter(f, true);
             BufferedWriter bw = new BufferedWriter(fw);
             PrintWriter out = new PrintWriter(bw)) {

            if (writeHeader) out.println(VehicleClass.csvHeader());
            for (VehicleClass v : vehicles) out.println(v.toCsvRow());
        } catch (IOException e) {
            System.out.println("Error appending CSV: " + e.getMessage());
        }
    }

    /** Convenience: append a single vehicle. */
    public static void append(String path, VehicleClass vehicle) {
        List<VehicleClass> one = new ArrayList<>();
        one.add(vehicle);
        append(path, one);
    }

    /** Read CSV and return each data line split by commas (header is skipped). */
    public static List<String[]> readRows(String path) {
        List<String[]> rows = new ArrayList<>();
        File f = new File(path);
        if (!f.exists()) return rows;

        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
            String line; boolean first = true;
            while ((line = br.readLine()) != null) {
                if (first) { first = false; continue; }   // skip header
                if (line.isBlank()) continue;
                rows.add(line.split(",", -1));            // naive split
            }
        } catch (IOException e) {
            System.out.println("Error reading CSV: " + e.getMessage());
        }
        return rows;
    }
}
