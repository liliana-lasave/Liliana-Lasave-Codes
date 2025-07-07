import java.util.Scanner;

public class SimpleNumbering {
    public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

        System.out.print("Enter a first number (lower integer): ");
        int firstNumber = input.nextInt();

        System.out.print("Enter a second number (higher integer): ");
        int secondNumber = input.nextInt();

        System.out.print("Enter a step (integer): ");
        int step = input.nextInt();

        System.out.println("Your numbers are: ");


        for (int i = firstNumber; i <= secondNumber; i = i + step) {
            System.out.println(i);
        }
    }
}

