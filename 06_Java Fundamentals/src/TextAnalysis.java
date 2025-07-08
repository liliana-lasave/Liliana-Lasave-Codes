// This program analyzes a text entered by the user
// It counts vowels, consonants, sentences, numbers, spaces, and other characters
//-------------------------------------------------------------------------------


import java.util.Scanner; // Import Scanner class for user input

public class TextAnalysis {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); // Create Scanner object

        // Ask the user to enter a text and read the input
        System.out.print("Enter your text: ");
        String userText = input.nextLine();

        // Initialize counters for vowels, consonants, sentences, spaces, numbers, and other characters
        int vowelCounter = 0;
        int consonantCounter = 0;
        int sentenceCounter = 0;
        int spaceCounter = 0;
        int numberCounter = 0;
        int otherCounter = 0; // Counter for other characters (symbols, etc.)

        // Define vowels (both lowercase and uppercase)
        String vowels = "aeiouAEIOU";

        // Define sentence-ending characters
        String endingSentence = ".?!:";

        // Define consonants (both lowercase and uppercase)
        String consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";

        // Define numbers (digits 0-9)
        String numbers = "0123456789";

        // Loop through each character of the text entered by the user
        for (int i = 0; i < userText.length(); i++) {
            char ch = userText.charAt(i); // Get the character at position i

            // indexOf() returns the index if 'ch' exists in the string, or -1 if not

            if (vowels.indexOf(ch) >= 0) {
                vowelCounter++;
            } else if (consonants.indexOf(ch) >= 0) {
                consonantCounter++;
            } else if (endingSentence.indexOf(ch) >= 0) {
                sentenceCounter++;
            } else if (numbers.indexOf(ch) >= 0) {
                numberCounter++;
            } else if (ch == ' ') {
                spaceCounter++;
            } else {
                otherCounter++;
            }
        }

        // Print out the results to the console
        System.out.println("There are    ➡️ " + vowelCounter + " vowels in your text.");
        System.out.println("There are    ➡️ " + consonantCounter + " consonants in your text.");
        System.out.println("There are    ➡️ " + sentenceCounter + " sentences in your text.");
        System.out.println("There are    ➡️ " + spaceCounter + " spaces in your text.");
        System.out.println("There are    ➡️ " + numberCounter + " numbers in your text.");
        System.out.println("There are    ➡️ " + otherCounter + " other characters in your text.");

        // Print the total length of the text (number of characters including letters, punctuation, spaces, numbers, and symbols)
        System.out.println("The text has ➡️ " + userText.length() + " characters.");

        input.close(); // Close the Scanner to avoid resource leaks
    }
}









