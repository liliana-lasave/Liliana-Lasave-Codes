import java.time.LocalTime;
import java.time.Duration;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

import java.util.Scanner;



public class Lasave_KMS_06_LE_07_01 {
    public static void main(String[] args) {
    Scanner input = new Scanner (System.in);

        // Ask the user to enter the time he started and finished the work and read it
        System.out.print("Enter the start time (HH:mm): ");
        String startTimeString = input.nextLine();
        LocalTime start = LocalTime.parse(startTimeString);

        System.out.print("Enter the end time (HH:mm): ");
        String endTimeString = input.nextLine();
        LocalTime end = LocalTime.parse(endTimeString);

        // Calculate the difference
        Duration workingTime = Duration.between(start, end);        // Duration calculates the difference between to times. It stores the time in nanoseconds.
        long hours = workingTime.toHours();                     // Converts the total duration to whole hours (ignores the remaining minutes).
        long minutes = workingTime.toMinutes() % 60;            // Converts the total duration to minutes. % 60 gives the rest of the division, to get the left minutes.

        System.out.println("\nStart: " + start);
        System.out.println("End: " + end);
        System.out.println("\nWorked time: " + hours + " hours and " + minutes + " minutes ");



        // Ask the user to enter the order date and the delivery date and read it
        System.out.print("\nEnter the order date (yyyy-MM-dd): ");
        LocalDate order = LocalDate.parse(input.nextLine());


        System.out.print("Enter the delivery date (yyyy-MM-dd): ");
        LocalDate delivery = LocalDate.parse(input.nextLine());



        // Calculate the delivery time
        long days = ChronoUnit.DAYS.between(order, delivery);

        System.out.println("\nOrder: " + order);
        System.out.println("Delivery: " + delivery);
        System.out.println("The delivery process takes: " + days + " day(s).");

        input.close();
    }
}
