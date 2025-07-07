import java.util.Scanner;                               // Import Scanner class to read user input

public class SimpleCalculatorOptimized {                // Define the class SimpleCalculatorOptimized
    public static void main(String[] args) {            // Main method to run the program
        Scanner input = new Scanner(System.in);         // Create Scanner object to read input

        // Call method to read the first number
        double firstNumber = readNumber(input, "Enter first number: ");

        // Call method to read the operator as a String
        String operator = readOperator(input, "Enter operator (+, -, *, /): ");

        // Call method to read the second number
        double secondNumber = readNumber(input, "Enter second number: ");

        // Call method to calculate the result based on inputs
        double result = calculate(firstNumber, secondNumber, operator);

        // Check if result is a valid number (it checks if result is not 'Not a Number') and print it
        if (!Double.isNaN(result)) {
            System.out.println("Result is: " + result);
        }

        input.close();                                  // Close Scanner to free resources
    }

    // Method to read a number from the user input
    public static double readNumber(Scanner input, String message) {
        System.out.print(message);                      // Print message prompt
        return input.nextDouble();                      // Read and return double value
    }

    // Method to read the operator from user input as String
    public static String readOperator(Scanner input, String message) {
        System.out.print(message);                      // Print message prompt
        return input.next();                            // Read the next token and return string input
    }

    // Method to perform calculation based on operator using modern switch expression
    public static double calculate(double num1, double num2, String op) {
        return switch (op) {
            case "+" -> num1 + num2;                    // Addition
            case "-" -> num1 - num2;                    // Subtraction
            case "*" -> num1 * num2;                    // Multiplication
            case "/" -> {
                if (num2 != 0) {
                    yield num1 / num2;                  // Similar to return but inside a switch expression
                } else {
                    System.out.println("Cannot divide by 0");    // Print error for division by zero
                    yield Double.NaN;                           // Return a special value meaning “not a valid number”
                }

            }
            default -> {                                        // Default is like "else" from switch
                System.out.println("Invalid operator");         // Print error for invalid operator
                yield Double.NaN;                               // Return "Not a Number" for invalid input
            }
        };          // it needs ; because I am using switch as an expression that returns a value
    }
}
