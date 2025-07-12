import java.util.Scanner;

public class Lasave_KMS_06_LE_05_01 {
    public static void main(String[] args) {
    Scanner input = new Scanner(System.in);


        // Ask the user to enter a valid color code
        System.out.print("Enter a color code (format: #018CFF): ");
        String colorInput = input.nextLine();

        // Convert the input to upper case
        colorInput = colorInput.toUpperCase();

        // Validate colorInput
        if (!colorInput.matches("^#[0-9A-F]{6}$")) {
            System.out.println("Invalid color code. Exiting the program.");
                    System.exit(1);  // Exit the program with status code 1 (means error)
        }

        // Extract the different components (red, green, blue)
        String redHex = colorInput.substring(1,3);
        String greenHex = colorInput.substring(3,5);
        String blueHex = colorInput.substring(5,7);

        // Convert to decimal
        int redValue = Integer.parseInt(redHex, 16);            // R = 1
        int greenValue = Integer.parseInt(greenHex, 16);            // G = 140
        int blueValue = Integer.parseInt(blueHex, 16);           // B = 255

        // Show results
        System.out.println("Red value: " + redValue);
        System.out.println("Green value: " + greenValue);
        System.out.println("Blue value: " + blueValue);
    }
}
