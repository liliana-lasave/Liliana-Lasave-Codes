import java.util.Scanner;                   // Import Scanner class to read user input

public class ShapesCalculator {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Show menu options to user
        System.out.println("Choose an option:");
        System.out.println("1. Calculate area of rectangle");
        System.out.println("2. Calculate area of equilateral triangle");
        System.out.println("3. Calculate area of circle");
        System.out.println("4. Calculate volume of cuboid");
        System.out.println("5. Calculate volume of triangular prism");
        System.out.println("6. Calculate volume of cylinder");

        // Read user choice
        int userChoice = input.nextInt();

        // Switch to call correct calculation method
        switch (userChoice) {
            case 1 -> {
                System.out.print("Enter length: ");
                double length = input.nextDouble();

                System.out.print("Enter width: ");
                double width = input.nextDouble();

                double area = areaRectangle(length, width);
                System.out.println("Area of rectangle is: " + area);
            }

            case 2 -> {
                System.out.print("Enter side: ");
                double side = input.nextDouble();

                double area = areaEquilateralTriangle(side);
                System.out.println("Area of equilateral triangle is: " + area);
            }

            case 3 -> {
                System.out.print("Enter radius: ");
                double radius = input.nextDouble();

                double area = areaCircle(radius);
                System.out.println("Area of circle is: " + area);
            }

            case 4 -> {
                System.out.print("Enter length: ");
                double length = input.nextDouble();

                System.out.print("Enter width: ");
                double width = input.nextDouble();

                System.out.print("Enter height: ");
                double height = input.nextDouble();

                double volume = volumeCuboid(length, width, height);
                System.out.println("Volume of cuboid is: " + volume);
            }

            case 5 -> {
                System.out.print("Enter side: ");
                double side = input.nextDouble();

                System.out.print("Enter length: ");
                double length = input.nextDouble();

                double volume = volumeTriangularPrism(side, length);
                System.out.println("Volume of triangular prism is: " + volume);
            }

            case 6 -> {
                System.out.print("Enter radius: ");
                double radius = input.nextDouble();

                System.out.print("Enter height: ");
                double height = input.nextDouble();

                double volume = volumeCylinder(radius, height);
                System.out.println("Volume of cylinder is: " + volume);
            }

            default -> System.out.println("Invalid choice. Please run again.");
        }

        input.close();
    }



    // Method to calculate area of rectangle
    public static double areaRectangle(double length, double width) {
        double result = length * width;                                          // Calculates area
        return result;                                                          // Return result
    }

    // Method to calculate area of equilateral triangle
    public static double areaEquilateralTriangle(double side) {
        double result = Math.sqrt(3) / 4 * Math.pow(side, 2);
        return result;
    }

    // Method to calculate area of circle
    public static double areaCircle(double radius) {
        double result = Math.PI * Math.pow(radius, 2);
        return result;
    }

    // Method to calculate volume of cuboid
    public static double volumeCuboid(double length, double width, double height) {
        double baseArea = areaRectangle(length, width);
        double result = baseArea * height;
        return result;
    }

    // Method to calculate volume of triangular prism
    public static double volumeTriangularPrism(double side, double length) {
        double baseArea = areaEquilateralTriangle(side);
        double result = baseArea * length;
        return result;
    }

    // Method to calculate volume of cylinder
    public static double volumeCylinder(double radius, double height) {
        double baseArea = areaCircle(radius);
        double result = baseArea * height;
        return result;
    }
}







