
import java.util.Scanner;

public class Lasave_KMS_06_LE_05_02 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Ask the user to enter an IP address
        System.out.print("Enter a valid IP address (like 192.168.0.1): ");
        String inputIdAddress = input.nextLine();

        // Split the address in 4 octets and store them in a string array
        String [] octetosIdAddress = inputIdAddress.split("\\.");

        // Declare an integer array with 4 places reserved
        int [] numerosInteger = new int[4];     // Reservo espacio para 4 numeros enteros

        // Loop to go through the octet array converting each element in an integer, which will be stored in the new integer array, at the same position
        for (int i = 0; i < octetosIdAddress.length; i++) {
            numerosInteger[i] = Integer.parseInt(octetosIdAddress[i]);
        }
        // Print labels for the table
        System.out.printf("\n||%10s|%10s|%8s|%14s||\n", "Decimal", "Binario", "Octal", "Hexadecimal");

        // Loop to go through the integer array, converting each element in strings that represent the same number in different systems (binary, octal, hexadecimal)
        for (int i = 0; i < numerosInteger.length; i++) {
            int decimal = numerosInteger[i];         // Save each integer in a temporal variable called decimal, out of practicity, not to write numerosInteger[i] many times
            String binario = String.format("%8s", Integer.toBinaryString(decimal)).replace(' ', '0');
            String octal = Integer.toOctalString(decimal);
            String hexadecimal = Integer.toHexString(decimal).toUpperCase();

            System.out.printf("||%10d|%10s|%8s|%14s||\n", decimal, binario, octal, hexadecimal);
        }
        input.close();
    }
}
