import java.util.Scanner;
import java.util.Random;
import java.util.Arrays;

public class Lasave_KMS_06_LE_06_03 {
    public static void main(String[] args) {
        Random rand = new Random();
        Scanner input = new Scanner(System.in);

        // 1) Generate a random array of 20 numbers between 1 and 10
        int[] randomArray = new int[20];

        for (int i = 0; i < randomArray.length; i++) {
            randomArray[i] = rand.nextInt(11);
        }


        // 2) Ask user to give a 4-digits sequence
        int[] sequenceUser = new int[4];

        System.out.println("Enter a sequence of 4 integers between 0 and 10: ");

        for (int i = 0; i < 4; i++) {
            System.out.print("Number " + (i + 1) + ": ");

            while (true) {
                if (input.hasNextInt()) {
                    sequenceUser[i] = input.nextInt();
                    break;
                } else {
                    System.out.print("Invalid input. Try again: ");
                    input.next();
                }
            }
        }


    // 3) Check if the sequence is in the array
        boolean found = false;

        int position = -1;

        for (int i = 0; i <= randomArray.length - sequenceUser.length; i++) {
            boolean match = true;
            for (int j = 0; j < sequenceUser.length; j++) {
                if (randomArray[i + j] != sequenceUser[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                found = true;
                position = i;
                break;
            }
        }

    // 4) Show results
        System.out.println("\nRandomly generated array: " + Arrays.toString(randomArray) + "\n");

        System.out.println("Sequence                : " + Arrays.toString(sequenceUser) + "\n");


        if (found) {
            System.out.println("The sequence was found in the position " + position + "   🥳");
        } else {
            System.out.println("Sequence not found 🥺");
        }
        input.close();
    }
}
