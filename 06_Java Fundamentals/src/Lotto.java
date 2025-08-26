import java.util.Arrays;
import java.util.Scanner;

public class Lotto {

    // --- Task rules as constants (easy to change if needed) ---
    private static final int COUNT = 6;  // how many lottery numbers
    private static final int MIN = 1;    // minimum allowed value (inclusive)
    private static final int MAX = 45;   // maximum allowed value (inclusive)

    /*
     * fixes suffixes on the numbers
     *
     */
    private static String ordinal(int n) {
        int mod100 = n % 100;
        if (mod100 >= 11 && mod100 <= 13) return n + "th";
        switch (n % 10) {
            case 1: return n + "st";
            case 2: return n + "nd";
            case 3: return n + "rd";
            default: return n + "th";
        }
    }

    /*
     * check if the current number has already been places in the list
     */
    private static boolean containsFirstN(int[] arr, int filled, int value) {
        for (int i = 0; i < filled; i++) {
            if (arr[i] == value) return true;
        }
        return false;
    }

    /*
     * Reads COUNT lottery numbers from the user.
     * - Only integers are accepted (uses try-catch).
     * - Each number must be between MIN and MAX (inclusive).
     * - No duplicates are allowed.
     * - On error, the user is prompted to re-enter.
     * Returns the numbers sorted in ascending order as an int[].
     */
    public static int[] readLottoNumbers(Scanner in) {
        int[] numbers = new int[COUNT];
        int filled = 0;

        while (filled < COUNT) {
            System.out.print("Enter the " + ordinal(filled + 1) + " number: ");

            try {
                // read and parse line
                String token = in.nextLine().trim();
                int value = Integer.parseInt(token); // may throw NumberFormatException

                // check if in range
                if (value < MIN || value > MAX) {
                    System.out.println("The number must be between " + MIN + " and " + MAX + ". Please repeat!");
                    continue; // ask again
                }

                // if number has been selected already, print error and try again
                if (containsFirstN(numbers, filled, value)) {
                    System.out.println("You have already entered this number. Please enter again!");
                    continue; // ask again
                }

                // place new number into list
                numbers[filled++] = value;

            } catch (NumberFormatException ex) {
                // Handles non-numeric input like "abc"
                System.out.println("This is not a number. Please repeat!");
            }
        }

        // sort the numbers before printing ticket
        Arrays.sort(numbers);
        return numbers;
    }

    public static void main(String[] args) {
        System.out.println("Lotto program started...");
        Scanner in = new Scanner(System.in);

        int[] result = readLottoNumbers(in);

        System.out.println("These are your lottery numbers: " + Arrays.toString(result));
        in.close();
    }
}
