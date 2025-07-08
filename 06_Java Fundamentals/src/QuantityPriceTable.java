import java.util.Scanner;

public class QuantityPriceTable {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String padded;
        int numSteps = 10;
        int priceLow;
        int priceHigh;
        int quantityLow = 2;
        int quantityHigh = 20;

        System.out.print("Enter a low price (integer): ");
            priceLow = input.nextInt();

        System.out.print("Enter a high price (integer): ");
        priceHigh = input.nextInt();


        int priceStep = (priceHigh - priceLow) / (numSteps - 1);
        int quantityStep = (quantityHigh - quantityLow)/ (numSteps - 1);;




        // Print label price on top of table
        System.out.println("👇 Quantity " + "        " + "Price 👉");
        System.out.print("     ");
        for (int p = priceLow; p <= priceHigh; p = p + priceStep) {
            padded = String.format("%5d", p);  // 5 characters wide
            System.out.print("     " + padded);
        }
        System.out.println("    " + "\n");



        for (int q = quantityLow; q <= quantityHigh; q = q + quantityStep) {
            padded = String.format("%5d", q);  // 5 characters wide
            System.out.print(padded + "     ");
            for (int p = priceLow; p <= priceHigh; p = p + priceStep) {
                int totalCost = q * p;
                padded = String.format("%5d", totalCost);  // 5 characters wide
                System.out.print(padded + "     ");
            }
            System.out.println("    ");
        }
    }


}

