import java.util.Random;
import java.util.Scanner;

public class Lasave_KMS_06_LE_04_03 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Ask the user to enter a number of surveyed (n, integer)
        System.out.print("Enter a number of surveyed to review the product (positive integer): ");
        int nInput = input.nextInt();

        int result;
        int ninput = 0;


        Random aleatoryNumber = new Random();   // Generates the generator of aleatory numbers

        int countOne = 0, countTwo = 0, countThree = 0;

        // Generate random numbers for the result array
        for (int i = 0; i < nInput; i++) {
            result = aleatoryNumber.nextInt(3) + 1;   // Generates 0, 1, 2, so when we add 1, we obtain 1, 2, 3.


            switch (result) {
                case 1:
                    countOne++;
                    break;
                case 2:
                    countTwo++;
                    break;
                case 3:
                    countThree++;
                    break;
            }
        }
        System.out.println("------------------------------------------------------");

        System.out.println("The number of not acceptable reviews is:  " + countOne);
        System.out.println("The number of acceptable reviews is:      " + countTwo);
        System.out.println("The number of excellent reviews is:       " + countThree);
        System.out.println("------------------------------------------------------");
        double percentageNotAccept = ((double) countOne / nInput) * 100.0;
        System.out.printf("The percentage of reviews as not acceptable was:  %.2f %%\n", percentageNotAccept);

        double percentageAccept = ((double) countTwo / nInput) * 100.0;
        System.out.printf("The percentage of reviews as acceptable was:      %.2f %%\n", percentageAccept);

        double percentageExcel = ((double) countThree / nInput) * 100.0;
        System.out.printf("The percentage of reviews as excellent was:       %.2f %%\n", percentageExcel);
        System.out.println("------------------------------------------------------");

        if (percentageNotAccept > percentageAccept && percentageNotAccept > percentageExcel) {
            System.out.println("The majority of respondents felt that the product is not acceptable.");
        }
        else if (percentageAccept > percentageNotAccept && percentageAccept > percentageExcel) {
                System.out.println("The majority of respondents felt that the product is acceptable.");
        }
        else {
            System.out.println("The majority of respondents felt that the product is excellent.");
        }
    }
}
