// Name: Liliana Lasave
// Assignment: Simple Calculator
// Date: 02.07.2025



import java.util.Scanner;                                   // Import the Scanner class to read user input


public class SimpleCalculator {                             // Define the class SimpleCalculator
    public static void main(String[] args) {                // Main method to run the program

        Scanner input = new Scanner(System.in);             // Create a Scanner object called input

        System.out.print("Enter first number: ");           // Ask user to enter the first number
        double firstNumber = input.nextDouble();            // Read the first number as double

        System.out.print("Enter operator (+,-,*,/): ");     // Ask user to enter an operator
        char operator = input.next().charAt(0);             // Read the operator as first character of input

        System.out.print("Enter second number: ");          // Ask user to enter the second number
        double secondNumber = input.nextDouble();           // Read the second number as double

        double result = 0;                                  // Declare and initialize result variable with 0

        if (operator == '+') {                              // Check if operator is '+'
            result = firstNumber + secondNumber;            // Calculate addition
            System.out.println("Result is: " + result);     // Print the result
        } else if (operator == '-') {                       // Check if operator is '-'
            result = firstNumber - secondNumber;            // Calculate subtraction
            System.out.println("Result is: " + result);     // Print the result
        } else if (operator == '*') {                       // Check if operator is '*'
            result = firstNumber * secondNumber;            // Calculate multiplication
            System.out.println("Result is: " + result);     // Print the result
        } else if (operator == '/') {                       // Check if operator is '/'
            if (secondNumber != 0) {                        // Check division by zero
                result = firstNumber / secondNumber;        // Calculate division
                System.out.println("Result is: " + result); // Print the result
            } else {
                System.out.println("Cannot divide by 0");   // Print error if dividing by zero
            }
        } else {
            System.out.println("Invalid operator");         // Print error for invalid operator
        }

        input.close();                                      // Close the Scanner to free resources
    }
}
