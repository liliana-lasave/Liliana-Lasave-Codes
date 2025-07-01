// This line imports Scanner to read user input
import java.util.Scanner;

public class UserInput { // This is the class!!!!!
public static void main(String[] args) {  // This is the main method!!!!!

    // Create a Scanner object called input to read input from the keyboard!!!!!
    Scanner input = new Scanner(System.in);

    // Ask the user to enter their first name, without going to a new line!!!!!
    System.out.print("Please enter your first name: ");
    String firstName = input.nextLine(); // Read the first name

    // Ask the user to enter their last name
    System.out.print("Please enter your last name: ");
    String lastName = input.nextLine(); // Read the last name

    // Combine first and last name in uppercase (structure: variable.method())
    String fullName = firstName.toUpperCase() + " " + lastName.toUpperCase();

    // Print the changed name!!!!!
    System.out.println("Your name in uppercase is: " + fullName);

    // Print the length of the full name (including space)
    System.out.println("Your full name has " + fullName.length() + " characters.");

    // Print the first letter of each name (initials)
    System.out.println("First initials: " + firstName.charAt(0) + "" + lastName.charAt(0));

    // Close the Scanner (Good practice to free computer memory)!!!!!
    input.close();
    }  // To close the main method

}  // To close the class