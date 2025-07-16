public class Lasave_KMS_06_LE_06_04 {
    public static void main(String[] args) {


        String colorString = "255,110,150";

        // Split the text string in 3 parts and store it in a text array
        String[] threeParts = colorString.split(",");

        // Check if the array has 3 parts
        if (threeParts.length != 3) {
            System.out.println("Error. The input should have three integer numbers separated by ','.");
            return;
        }

        // Convert the text-array into integer-array, to be able to perform maths
        int[] threeNumbers = new int[3];

        for (int i = 0; i < 3; i++) {
            threeNumbers[i] = Integer.parseInt(threeParts[i]);
        }

        for (int i = 0; i < threeParts.length; i++) {
            if (threeNumbers[i] > 255 || threeNumbers[i] < 0) {
                System.out.println("Error. Each integer number should be between 0 and 255.");
                return;
            }

        }

        // Convert the RGB color code into CMY code
        double c = (255 - threeNumbers[0])/ 255.0 * 100;

        double m = (255 - threeNumbers[1])/ 255.0 * 100;

        double y = (255 - threeNumbers[2])/ 255.0 * 100;

        // Show results
        System.out.println("CMY values: ");

        System.out.printf("C = %.2f\n", c);
        System.out.printf("M = %.2f\n", m);
        System.out.printf("Y = %.2f\n", y);
    }
}
