import java.util.Scanner;

public class Lasave_KMS_06_LE_04_05 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Read input
        String input1 = readInput(input, "Enter number 1: ");
        String input2 = readInput(input, "Enter number 2: ");

        double number1 = parseInput(input1);
        double number2 = parseInput(input2);

        // Read operator
        String operator = readOperator(input);

        // Calculator
        double result = calculate(number1, number2, operator);

        // Show result
        System.out.printf("\nThe result of the calculation is: %.2f\n", result);
        input.close();
    }

    // Method readInput
    public static String readInput(Scanner input, String message) {
        System.out.print(message);
        return input.nextLine();
    }

    // Method parseInput
    public static double parseInput(String inputString) {
        inputString = inputString.replace(",", ".");
        return Double.parseDouble(inputString);
    }

    // Method readOperator
    public static String readOperator(Scanner input) {
        System.out.print("If you want to add, subtract, multiply or divide, enter +, * or / respectively: ");
        return input.nextLine();
    }

    // Method calculate
    public static double calculate(double number1, double number2, String operator) {
        switch (operator) {
            case "+":
                return add(number1, number2);

            case "-":
                return subtract(number1, number2);

            case "*":
                return multiply(number1, number2);

            case "/":
                if (number2 != 0) {
                    return divide(number1, number2);
                } else {
                    System.out.println("Error : It is not possible to divide by zero.");
                    return 0;
                }
            default:
                System.out.println("Error. Not valid operator.");
                return 0;
        }
    }

    // Math operations
    public static double add(double a, double b) {
        return a + b;
    }

    public static double subtract(double a, double b) {
        return a - b;
    }

    public static double multiply(double a, double b) {
        return a * b;
    }

    public static double divide(double a, double b) {
        return a / b;
    }


}