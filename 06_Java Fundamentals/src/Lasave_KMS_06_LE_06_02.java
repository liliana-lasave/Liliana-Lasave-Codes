public class Lasave_KMS_06_LE_06_02 {
    public static void main(String[] args) {
        System.out.println();
        System.out.println("First set of numbers:");
        System.out.println();
        add(1, 2, 3);
        System.out.println("-----------------------------");

        System.out.println();
        System.out.println("Second set of numbers:");
        System.out.println();
        add(2, 6, 8, 3);
        System.out.println("-----------------------------");



    }

    // Method to add all the numbers that are in each list
    public static void add(int ... numbers) {
        int addition = 0;

        for (int n : numbers) {
            addition += n;      // To add each number
        }
    // Show amount of numbers and result of the additions
    System.out.println("There are " + numbers.length + " numbers.");
    System.out.println();
    System.out.println("The sum of all the numbers is equal to " + addition + ".");

    }
}
