import java.util.Scanner;

public class YearRange {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a starting year: ");
        int lowYear = input.nextInt();
        System.out.print("Enter an ending  year: ");
        int highYear = input.nextInt();

        for (int year = lowYear; year <= highYear; year++) {

            checkIfLeapYear(year);

        }
        input.close();
    }

    public static void checkIfLeapYear(int year) {
        if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) {
            System.out.println("You entered    " + year +    ", which is a leap year     (●'◡'●)");
        } else {
            System.out.println("You entered    " + year +    ", which is a not leap year (❁´◡`❁)");
        }
    }
}


