import java.util.*;                             // List and other collection utilities
import java.nio.file.*;                         // Path and Files for filesystem operations
import java.io.*;                               // IOException and general I/O classes

public class CsvManager {                       // Utility class that only holds static methods
    private CsvManager() {} // utility class    // Private constructor: prevents creating objects of this class


    // Give me file to write, loop through the animal list and write the formatted info in the list and leave
    public static void save(String fileName, List<Animal> animalList) {
        try {
            FileWriter animalFile = new FileWriter(fileName);           // Create a new file called animalFile

            for (Animal animalItem : animalList) {
                animalFile.write(animalItem.toString() + "\n");     // write out the csv formatted
            }

            animalFile.close();
            System.out.println("Saved to: " + fileName);
        } catch (IOException ioException) {
            System.out.println("Save error: " + ioException.getMessage());
        }
    }

        // Loads the animalList from CSV file and returns next available ID:
    public static int load(String file, List<Animal> animalList, int minId) {
        // it is not necessary to clear again
        animalList.clear();

        Path path = Path.of(file);

        if (!Files.exists(path)) {          // if the file does not exist: set the minId and quit the code
            System.out.println("No file yet. It will be created on save at: " + path.toAbsolutePath());
            return minId; // start IDs at
        }

        int maxIdSeen = -1;          // keep an eye for the maximum ID
        try {
            for (String rawLine : Files.readAllLines(path)) {           // reads in the CSV file
                String line = rawLine.trim();

                // Split the lines and assign the strings one by one
                String[] columns = line.split(",");
                int animalId    = Integer.parseInt(columns[0].trim());
                String animalType = columns[1].trim();
                String name     = columns[2].trim();
                int animalAge   = Integer.parseInt(columns[3].trim());
                String extra1   = columns[4].trim();
                String extra2   = columns[5].trim();

                // Creates objects according to the animalType
                Animal animalItem;
                if ("DOG".equalsIgnoreCase(animalType)) {                 // Compares text from CSV (animalType) with "DOG", ignoring capital letters/lowercases
                    animalItem = new Dog(animalId, name, animalAge, extra1, extra2); // create a new Dog
                } else if ("CAT".equalsIgnoreCase(animalType)) {
                    animalItem = new Cat(animalId, name, animalAge, extra1, extra2);
                } else {
                    System.out.println("Unknown animal type: " + animalType);
                    continue;       // continue
                }

                animalList.add(animalItem);

                if (animalId > maxIdSeen) maxIdSeen = animalId;     // looks for the highest animalId in the list
            }
            System.out.println("Loaded " + animalList.size() + " animals from: " + path.toAbsolutePath());

        } catch (Exception exception) {
            System.out.println("Load error: " + exception.getMessage());        // if an error occurs, it creates an object exception and calls the method getMessage()
        }

        return maxIdSeen + 1; // next available ID
    }
}
