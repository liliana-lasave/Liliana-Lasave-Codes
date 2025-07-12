import java.util.Scanner;

public class Lasave_KMS_06_LE_05_03 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);


        // Ask the user to enter a string
        System.out.print("Enter a string (format: article:[name of the article]order:[name of the buyer]): ");
        String text = input.nextLine();

        // Find the indexes where certain article starts and ends
        int startArticle = text.indexOf("article:[") + "article:[".length();
        int endArticle = text.indexOf("]", startArticle);       // looks for the index of the first ] after the index of startArticle

        // Find the substring corresponding to the article
        String article = text.substring(startArticle,endArticle);
        System.out.print("\n📦 Article:\t\t" + article + "\n");


        // Find the indexes where the name of the client starts and ends
        int startName = text.indexOf("order:[") + "order:[".length();
        int endName = text.indexOf("]", startName);       // looks for the index of the first ] after the index of startName

        // Find the substring corresponding to the name of the client
        String name = text.substring(startName,endName);
        System.out.println("\n👤 Client :\t\t" + name);

        System.out.print("\n➡️ The " + article + " was ordered by " + name + ".\n");

        input.close();
    }

}
