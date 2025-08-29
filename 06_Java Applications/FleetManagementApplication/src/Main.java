//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        // Create a car (object)
        CarClass myFirstCar = new CarClass("Steamer", 1949, "water"); // (String modelIn, int yearIn, String engineTypeIn)

        // Create other car (object)
        CarClass mySecondCar = new CarClass("HydroCar", 2026, "H2"); // (String modelIn, int yearIn, String engineTypeIn)

        // Show cars info
        myFirstCar.showVehicleInfo();
        mySecondCar.showVehicleInfo();

        myFirstCar.addFuel(10);
        myFirstCar.addFuel(5);
        int fuelLiters = myFirstCar.getFuelAmount();
        System.out.println("My " + myFirstCar.model + " got " + fuelLiters + " liters of " + myFirstCar.engineType + ".");

        mySecondCar.addFuel(50);
        fuelLiters = mySecondCar.getFuelAmount();
        System.out.println("My " + mySecondCar.model + " got " + fuelLiters + " liters of " + mySecondCar.engineType + ".");


        //-------------------------------------------
        // Create a truck (object)
        TruckClass myFirstTruck = new TruckClass("FleetStar", 1960, "1 Ton");

        // Create other truck (object)
        TruckClass mySecondTruck = new TruckClass("FleetGiant", 2000, "10 Ton");

        // Show trucks info
        myFirstTruck.showVehicleInfo();
        mySecondTruck.showVehicleInfo();

        myFirstTruck.addFuel(100);
        myFirstTruck.addFuel(56);
        fuelLiters = myFirstTruck.getFuelAmount();
        System.out.println("My " + myFirstTruck.model + " got " + fuelLiters + " liters of biodiesel.");

        mySecondTruck.addFuel(50);
        fuelLiters = mySecondTruck.getFuelAmount();
        System.out.println("My " + mySecondTruck.model + " got " + fuelLiters + " liters of biodiesel.");


        // Show number of cars
        System.out.println("I have " + CarClass.numberOfCars + " cars.");;

        // Show number of trucks
        System.out.println("I have " + TruckClass.numberOfTrucks + " trucks.");;

        // Show number of vehicles
        System.out.println("I have " + VehicleClass.numberOfVehicles + " vehicles in total.");;

        //-------------------------------------------------------------

        // Create a motorcycle (object)
        MotorcycleClass myFirstMotorcycle = new MotorcycleClass("Sunshine", 1984, 60, "red"); //

        // Create other car (object)
        MotorcycleClass mySecondMotorcycle = new MotorcycleClass("Traveller", 2025, 75, "silver"); //

        // Show cars info
        myFirstMotorcycle.showVehicleInfo();
        mySecondMotorcycle.showVehicleInfo();

        myFirstMotorcycle.addFuel(6);
        myFirstMotorcycle.addFuel(5);
        fuelLiters = myFirstMotorcycle.getFuelAmount();
        System.out.println("My " + myFirstMotorcycle.model + " motorcycle, that is " + myFirstMotorcycle.color + ", got " + fuelLiters + " liters of petrol.");

        mySecondMotorcycle.addFuel(57);
        fuelLiters = mySecondMotorcycle.getFuelAmount();
        System.out.println("My " + mySecondMotorcycle.model + " motorcyle, that is " + myFirstMotorcycle.color + ", got " + fuelLiters + " liters of petrol.");

        //-------------------------------------------------------------

        // Create a bicycle (object)
        BicycleClass myFirstBicycle = new BicycleClass("Carina", 2000, "carbon", "road");

        // Create other car (object)
        BicycleClass mySecondBicycle = new BicycleClass("Marc", 2023, "titanium", "beach");

        // Show cars info
        myFirstBicycle.showVehicleInfo();
        mySecondBicycle.showVehicleInfo();



    }

}