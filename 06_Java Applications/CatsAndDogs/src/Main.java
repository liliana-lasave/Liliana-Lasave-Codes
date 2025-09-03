
import java.nio.file.*;     // important for Files (methods to read and write files) and Path (the path of a file or folder)


public class Main {
    static final String FILE = "animals.csv";       // Outside of main, constant (final) declaration of a String variable named FILE
                                                    // with value "animals.csv"

    public static void main(String[] args) throws Exception {       // throws Exception, if something goes wrong, the program gives an error
        Dog dog1 = new Dog("Bruni", 2, "meat");
        dog1.printInfo();

        Cat cat1 = new Cat("Mini", 3, "wild");
        cat1.printInfo();


        // Save in the file
        String content = dog1.toCsvRow() + "\n" + cat1.toCsvRow() + "\n";       // Build a String called content with 2 lines (dog and cat in CSV format)
        Files.writeString(Path.of(FILE), content);                               //  Write the content into the file "FILE" ("animals.csv").
                                                                                // If the file does not exist, it is created. If it exists, it is overwritten.



        // Now I will not print the lines like before, but we will format the lines in a way that we can reconstruct the info to feed the constructor again:

        System.out.println ("*************");

        // Read: open the file animals.csv and reads all the lines
        for (String line : Files.readAllLines(Path.of(FILE))) {
            String[] parts = line.split(",");       // Split text using commas "," as separator, and stores the parts in an array called parts.

            // Parse each part and remove quotes if present
            String animalType = parts[0];
            String name = parts[1];                  // for ex. "Bruna"
            int age = Integer.parseInt(parts[2]);       // for ex 3, converted from text to integer
            String extraInfo = parts[3];                  // "meat"

            if (animalType.equals("dog")) {
                Dog dog1Recreated = new Dog (name, age, extraInfo);
                dog1Recreated.printInfo();
            } else {
                Cat cat1Recreated = new Cat (name, age, extraInfo);
                cat1Recreated.printInfo();
            }
        }
    }
}







/*
    // With getters and setters and public attributes:
        System.out.println(myFirstAnimal.getName());        // Read the name con getter: Pepita

        myFirstAnimal.setName("Cotty");                     // Change the name with setter: Cotty

        System.out.println(myFirstAnimal.getName());        // Read the name con getter: Cotty

        System.out.println(myFirstAnimal.getAge());        // Read the age con getter: 1

        myFirstAnimal.setAge(2);                            // Change the age with setter: 2

        System.out.println(myFirstAnimal.getAge());        // Read the age con getter: 2
 /*
    // Without getters and setters and public atributes, anyone can modify the values of the attributes!

    System.out.println(myFirstAnimal.name);

    myFirstAnimal.name = "Cotorrita";

    System.out.println(myFirstAnimal.name);

    // Read: open the file animals.csv and reads all the lines
        //for (String line : Files.readAllLines(Path.of(FILE))) {                 // Open the file "animals.csv" and return all its lines as a List<String> (each line is a String). For iterates through the lines one by one and places them in the variable line.
            //System.out.println(line);                                           // Print each line:
                                                                                                        //Bruni,2,meat
                                                                                                        //Mini,3,wild
 */
