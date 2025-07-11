import java.util.Random;            // To use the methods of the Random class, we need to import them from the package
import java.util.Scanner;

public class Lasave_KMS_06_LE_04_04 {
    public static void main(String[] args) {
        Random generator = new Random();   // To create an object of the Random class named generator
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a number of samples: ");
        int totalDraws = input.nextInt();

        int i = 0;          // Before starting the loop, the variable i (counter of the loop) is created and initialized to 0.
        int maxNumber = 45;         // We declare the variable maxNumber to store the range of possible numbers in the lottery draw (numbers from 1 to 45). For that reason I initialize it with the value 45.

        int drawnNumber = 1;
        int [] frequency = new int[maxNumber];       // Array of the frequency (number of occurrences, each array position works as a counter) of each number, in the n lottery plays.

        for (i = 0; i < totalDraws; i++) {       // As long as drawCount < totalDraws, the loop will repeat. After each loop, drawCount is increased by 1.

            drawnNumber = generator.nextInt(maxNumber) + 1;// Generates a random number between 1 and 45 and stores it in the drawnNumber variable.

            frequency[drawnNumber - 1]++;           // // Increments by 1 the counting (frequency) of the aleatory number in the frequency array (subtract 1, to convert the number drawn to the correct index of the array.).

        }

        float percentFrequency = 0;


        // Loop to print the frequency and percentage of each number from 1 to 45
        for (i = 0; i < maxNumber; i++) {
            percentFrequency = ((float) frequency[i] / totalDraws) * 100;           // Calculate the percentage of appearance for each number
            System.out.printf("Number %d appeared %d times (%.2f %%)\n", (i + 1), frequency[i], percentFrequency);      // Print the results: integer number (%d, i+1), how many times it appeared (also %d), and its percentage (with 2 decimal places: %.2f)
        }
    }
}
