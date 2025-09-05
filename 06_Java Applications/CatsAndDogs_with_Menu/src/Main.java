

import java.util.ArrayList;                                                      // Imports the class ArrayList (dynamic list, that can grow or get smaller automatically)
import java.util.List;                                                           // Imports the interface List (interface defines a contract: a set of methods that a class must implement, but without saying how)
import java.util.Scanner;                                                        // Imports Scanner to read from Keyboard

public class Main {
    private static String ANIMAL_FILE = "animals.csv";                     // Name of the CSV file

    static List<Animal> animalList = new ArrayList<>();                      // static means that belongs to the class, no to each object. That means that there is only one database shared by the whole program
    static int nextId = 100;                                         // Global counter of IDs. Starts in 100. Each time I add a new animal, nextId is used and then it increases. In this way, each animal has a unique ID.

    public static void main(String[] args) {
        nextId = CsvManager.load(ANIMAL_FILE, animalList, nextId);  // load at start
/* The CsvManager loads data from the CSV file (animals.csv) and places them in the list `database`.
   At the same time returns the next ID available. This value is assigned to `nextId` so the next
   new animal continues numbering without duplicates. */

        Scanner input = new Scanner(System.in);        // creates a reader from the keyboard
        while (true) {                              // infinite loop until the user chooses to leave
            System.out.println("\n=== Animal Shelter ==="); // Menu showed in each iteration
            System.out.println("1) Add Dog");
            System.out.println("2) Add Cat");
            System.out.println("3) List all");
            System.out.println("4) Search (name/type/age/range/extra/any)");
            System.out.println("5) Delete by ID");
            System.out.println("6) Save CSV");
            System.out.println("0) Save & Exit");       // Break breaks the while(true)
            System.out.print("Choose: ");

            String option = input.nextLine().trim();  // Reads the input as text, applies the .trim method. Uses string instead of integer, to avoid conflicts in case the use writes letters.

            if (option.equals("1")) addDog(input);
            else if (option.equals("2")) addCat(input);
            else if (option.equals("3")) listAll();
            else if (option.equals("4")) search(input);
            else if (option.equals("5")) deleteById(input);
            else if (option.equals("6")) CsvManager.save(ANIMAL_FILE, animalList);
            else if (option.equals("0")) {
                CsvManager.save(ANIMAL_FILE, animalList); System.out.println("Bye!");
                break;
            }
            else System.out.println("Invalid option.");
        }
    }

    // ---- add ----
    static void addDog(Scanner input) {
        System.out.print("Name: ");
        String name = input.nextLine();
        int age = askInt(input, "Age: ");
        System.out.print("Breed: ");
        String breed = input.nextLine();
        System.out.print("Food type: ");
        String food = input.nextLine();
        Dog newDogItem = new Dog(nextId, name, age, breed, food);
        animalList.add(newDogItem);
        System.out.println("Dog added!");
        nextId++;
    }
    static void addCat(Scanner input) {
        System.out.print("Name: ");
        String name = input.nextLine();
        int age = askInt(input, "Age: ");
        System.out.print("Color: ");
        String color = input.nextLine();
        System.out.print("Origin: ");
        String origin = input.nextLine();
        Cat newCatItem = new Cat(nextId, name, age, color, origin);
        animalList.add(newCatItem);
        System.out.println("Cat added!");
        nextId++;
    }

    // List: if there are animals, print one per row; if there is no animals, it shows (empty).
    static void listAll() {
        if (animalList.isEmpty()) {
            System.out.println("(empty)");
            return;                             // get out of the method
        }
        for (Animal item : animalList) {        // go through each Animal in the list
            System.out.println(item);           // print the animal. This calls automatically to item.toString(). As toString() returns a CSV row, that row is printed.
        }
    }

    // Delete an individual animal from the list, if not found, print error message
    static void deleteById(Scanner input) {
        int idToDelete = askInt(input, "ID to delete: ");           // We will store an integer into the variable idToDelete. We call the helper: shows text in console, reads the input, parse the input and if it is not a number, keep asking for a valid input and gives back and int

        for(int i = 0; i < animalList.size(); i++) {
            Animal item = animalList.get(i);                                                          // Retrieves the item "i"

            if (item.getId() == idToDelete) {                                                       // Compares the numeric ID
                animalList.remove(i);                                                                 // Removes the i-th item from the animal list
                System.out.println("The animal with the ID " + idToDelete + " was removed.");
                CsvManager.save(ANIMAL_FILE, animalList);                                                    // Auto-save after deleting
                return;                                                                             // Gets out of the method, stop searching (we already removed the animal)
            }
        }
        System.out.println("There is no animal with the ID " + idToDelete + " in our shelter.");
    }

    // ---- SEARCH: name / type / age / range / extras / any ----
    static void search(Scanner input) {
        if (animalList.isEmpty()) {
            System.out.println("(empty)");
            return;
        }

        System.out.println("\nSearch by:");
        System.out.println(" 1) Name (contains)");
        System.out.println(" 2) Type (DOG/CAT)");
        System.out.println(" 3) Age (exact)");
        System.out.println(" 4) Age range (min..max)");
        System.out.println(" 5) Extra field (breed/food/color/origin)");
        System.out.println(" 6) Any text (matches anywhere)");
        System.out.print("Choose: ");
        String opt = input.nextLine().trim();

        List<Animal> results = new ArrayList<>();       // A list of whatever is searched for

        switch (opt) {
            case "1": { // name contains
                System.out.print("Name contains: ");
                String nameString = input.nextLine().trim().toLowerCase();
                for (Animal item : animalList)
                    if (contains(item.getName(), nameString)) results.add(item);
                break;
            }
            case "2": { // type equals
                System.out.print("Type (DOG/CAT): ");
                String inputText = input.nextLine().trim();
                for (Animal item : animalList)
                    if (item.type().equalsIgnoreCase(inputText)) results.add(item);
                break;
            }
            case "3": { // exact age
                int age = askInt(input, "Age = ");
                for (Animal item : animalList)
                    if (item.getAge() == age) results.add(item);
                break;
            }
            case "4": { // age range
                int min = askInt(input, "Min age: ");
                int max = askInt(input, "Max age: ");
                for (Animal item : animalList)
                    if (item.getAge() >= min && item.getAge() <= max) results.add(item);
                break;
            }
            case "5": { // extra fields
                System.out.print("Text in extras (breed/food/color/origin): ");
                String inputText = input.nextLine().trim().toLowerCase();
                for (Animal item : animalList) {
                    String[] extraText = item.extrasForCsv();
                    String extraText1 = extraText.length > 0 ? extraText[0] : "";
                    String extraText2 = extraText.length > 1 ? extraText[1] : "";

                    if (contains(extraText1, inputText) ||
                        contains(extraText2, inputText)) {
                        results.add(item);
                    }
                }
                break;
            }
            case "6": { // any text anywhere
                System.out.print("Search text anywhere: ");
                String searchText = input.nextLine().trim().toLowerCase();
                for (Animal item : animalList) {
                    String[] extraText = item.extrasForCsv();
                    String extraText1 = extraText.length > 0 ? extraText[0] : "";
                    String extraText2 = extraText.length > 1 ? extraText[1] : "";
                    String ageS = String.valueOf(item.getAge());
                    if (contains(item.getName(), searchText) ||
                        contains(item.type(),    searchText) ||
                        contains(extraText1,     searchText) ||
                        contains(extraText2,     searchText) ||
                        ageS.contains(searchText)) {
                        results.add(item);
                    }
                }
                break;
            }
            default:
                System.out.println("Invalid option.");
                return;
        }

        if (results.isEmpty()) System.out.println("No matches.");
        else {
            System.out.println("Results:");                             // Here is where the results of the search are printed
            for (Animal item : results) System.out.println(" * " + item);   //
        }
    }

    // Give an integer                                                       ask a number with the prompt, read the line, and try to convert it to an integer. Repeats this until it is a valid input, and returns a integer when the goal is achieved ----
    static int askInt(Scanner input, String prompt) {                       // static method that returns an integer, receives an input from scanner and a prompt to show the user
        while (true) {
            System.out.print(prompt);
            String text = input.nextLine().trim();
            try {
                return Integer.parseInt(text);                              // "risky" code: try to convert text to integer
            }
            catch (NumberFormatException ioException) {                               // if there is a mistake (letters, empty, numbers out of range) a message will be shown and we will ask again
                System.out.println("Write numbers only (e.g., 0, 1, 2).");
            }
        }
    }

    static boolean contains(String text, String qLower) {
        return text != null && text.toLowerCase().contains(qLower);
    }
}
