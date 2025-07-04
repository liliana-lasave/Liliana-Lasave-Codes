import java.util.Scanner;


public class ProductEntryValidation {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Read description first
        String description = readDescription(input, "Enter product description: ");

        //Read quantity
        int quantity = readPositiveInt(input, "Enter product quantity (positive integer): ");

        // Read price
        double price = readPositiveDouble(input, "Enter product price per unit (positive value): ");

        // Show result in one line separated by commas

        System.out.println("You entered: ");
        System.out.println("Description: " + description + " ,  Quantity: " + quantity + " ,  Price: " + price);

        // Close Scanner
        input.close();
    }

    // Keep asking the user for a valid description until not empty
    public static String readDescription(Scanner input, String message) {
        String desc = "";

        while (desc.isEmpty()) {
            System.out.println(message);
            desc = input.nextLine();

            if (desc.isEmpty()) {
                System.out.println("Invalid input.  Description cannot be empty");
                System.out.println("-------------------------------------------");
            }
        }
        return desc;
    }


    // Keep asking the user for a valid positive integer
    public static int readPositiveInt(Scanner input, String message) {
        int value = -1;

        while (value <= 0) {
            System.out.println(message);

            if (input.hasNextInt()) {
                value = input.nextInt();
                if (value <= 0) {
                    System.out.println("Invalid input. Please enter a positive integer.");
                }
            } else {
                System.out.println("Invalid input. Please enter numbers only.");
                input.next();   // Discard invalid input
            }
            System.out.println("-----------------------------------------------");
        }

    input.nextLine();   // Clear buffer to avoid skipping nextLine() after nextInt()/nextDouble()
    return value;
    }

    // Keep asking the user for a valid price until it is the case
    public static double readPositiveDouble(Scanner input, String message) {
        double value  = -1;

        while (value <= 0) {
            System.out.println(message);

            if (input.hasNextDouble()) {
                value = input.nextDouble();
                if (value <= 0) {
                    System.out.println("Invalid input. Please enter a positive value.");
                }
            } else {
                System.out.println("Invalid input. Please enter numbers only.");
                input.next();
            }
            System.out.println("---------------------------------------------");
        }
        input.nextLine();
        return value;
    }

}
