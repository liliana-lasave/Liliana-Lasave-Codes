import java.util.Scanner;

public class LeapYear {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);


        // Keep asking the user to enter a valid input and read the number
        while (true) {      // Infinite loop until something breaks it
            System.out.println("Enter a valid input (a positive integer): ");

            if (input.hasNextInt()) {   // Checks if the input is an integer
                int inputYear = input.nextInt();       // Read the integer
                if (inputYear > 0) {
                    checkIfLeapYear(inputYear);
                    break;      // Get out of the loop
                } else {
                    System.out.println("Invalid input. Enter a positive integer.");
                }
            } else {
                System.out.println("Invalid input. Enter a positive integer.");
                input.next();
            }
        }
        input.close();
    }
    public static void checkIfLeapYear(int inputYear) {
        if ((inputYear % 400 == 0) || (inputYear % 4 == 0 && inputYear % 100 != 0)) {
            System.out.println("You entered a leap year.");
        } else {
            System.out.println("The year is not a leap year.");
        }
    }
}

