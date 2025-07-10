import java.util.Scanner;

public class Lasave_KMS_1_05_LE_04_02 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);


        // Read a string to encrypt
        System.out.print("Enter a string: ");
        String stringToEncrypt = input.nextLine();

        // Convert the string to uppercase as I am also using capital letter in the encryption
        stringToEncrypt = stringToEncrypt.toUpperCase();

        // Read a shift value from user (it can also be a negative shift)
        System.out.print("Enter a shift: ");
        int hardShift = input.nextInt();

        System.out.print("The encrypted message is: ");

        // Loop through each character in the string
        for (int i = 0; i < stringToEncrypt.length(); i++) {
            char hardChar = stringToEncrypt.charAt(i); // get each character

            // Encrypt the character using the encryptedLetter method
            char encryptedMessage = encryptedLetter(hardChar, hardShift);

            // Print the encrypted character without line breaks
            System.out.print(encryptedMessage);
        }
    }

    public static char encryptedLetter(char hardChar, int hardShift) {

        // Define the English uppercase alphabet as an array
        char[] hardAlphabet = {
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z'
        };
        int i = 0;
        boolean found = false; // flag to check if character is in the alphabet

        // Check if character is a space or common punctuation
        if (hardChar == ' ' || hardChar == '.' || hardChar == ',' || hardChar == '!' ||
                hardChar == '?' || hardChar == ';' || hardChar == ':' || hardChar == '\'' ||
                hardChar == '"' || hardChar == '(' || hardChar == ')' || hardChar == '-' ||
                hardChar == '_' || hardChar == '[' || hardChar == ']' || hardChar == '{' ||
                hardChar == '}' || hardChar == '/' || hardChar == '\\' || hardChar == '@' ||
                hardChar == '#' || hardChar == '$' || hardChar == '%' || hardChar == '^' ||
                hardChar == '&' || hardChar == '*' || hardChar == '+' || hardChar == '=' ||
                hardChar == '<' || hardChar == '>' || hardChar == '`' || hardChar == '~' ||
                hardChar == '|') {
            return hardChar; // return punctuation and space without encryption
        }

        // Loop through the alphabet array to find the position of hardChar
        for (i = 0; i < hardAlphabet.length; i++) {
            if (hardAlphabet[i] == hardChar) {
                found = true;
                break; // exit the loop once found
            }
        }

        // If character not found in the alphabet, print error and exit program
        if (!found) {
            System.out.print("\n\nProgram error: character not found: " + hardChar);
            System.exit(0);
        }

        // Calculate the new index with the shift
        int newIndex = i + hardShift;

        // If newIndex is greater than or equal to the length, wrap around
        if (newIndex >= hardAlphabet.length) {
            newIndex = newIndex - hardAlphabet.length;
        }

        // If newIndex is negative, wrap around from the end of the alphabet
        if (newIndex < 0) {
            newIndex = newIndex + hardAlphabet.length;
        }

        // Get the encrypted character from the alphabet array
        char newHardChar = hardAlphabet[newIndex];

        // Return the encrypted character
        return newHardChar;
    }
}


