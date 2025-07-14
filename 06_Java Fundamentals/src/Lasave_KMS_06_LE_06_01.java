import java.util.Random;            // Import Random class from java.util package

public class Lasave_KMS_06_LE_06_01 {
    public static void main(String[] args) {

        int[] array = generateArray(100);

        System.out.println("Table:");
        formatArray(array, 10);

        int min = findMin(array);
        int max = findMax(array);

        System.out.println("\n Minimum: " + min);
        System.out.println("\n Maximum: " + max);
    }

    // Method to generate array
    public static int[] generateArray(int quantity) {
        int[] arrayRandNum = new int[quantity];       // Define an array of size "quantity" called arrayRandNum
        Random rand = new Random();                   // Creates a Random object called rand

        // Fill the array with aleatory numbers
        for (int i = 0; i < arrayRandNum.length; i++) {
            arrayRandNum[i] = rand.nextInt(10) + 1; // Aleatory numbers between 1 and 10 (inclusive)
        }
        return arrayRandNum;
    }


    // Method to print the numbers with a table format
    public static void formatArray(int[] arrayRandNum, int columnsPerLine){
        for (int i = 0; i < arrayRandNum.length; i++) {

            System.out.printf("%5d", arrayRandNum[i]);      // %5d aligns each number of the array to the right and has 5 spaces reserved

            if ((i + 1) % columnsPerLine == 0) {        // each "columnsPerLine" elements, go to a new line
                System.out.println();                   // Line break
            }
        }
        System.out.println();                   // Line break
    }

    // Method to find the min number in the array
    public static int findMin(int[] arrayRandNum){
        int minNumber = arrayRandNum[0];        // Initialize minNumber with the first element
        for (int i = 1; i < arrayRandNum.length; i++) {
            if (arrayRandNum[i] < minNumber) {
                minNumber = arrayRandNum[i];        // Update minNumber if a new one was found
            }
        }
        return minNumber;
    }

    // Method to find the max number in the array
    public static int findMax(int[] arrayRandNum){
        int maxNumber = arrayRandNum[0];        // Initialize maxNumber with the first element
        for (int i = 1; i < arrayRandNum.length; i++) {
            if (arrayRandNum[i] > maxNumber) {
                maxNumber = arrayRandNum[i];        // Update maxNumber if a new one was found
            }
        }
        return maxNumber;
    }
}

