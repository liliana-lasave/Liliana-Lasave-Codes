//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        System.out.println("======================================================================");
        System.out.println("CARS");
        System.out.println("======================================================================");

        // Create a car (object)
        CarClass myFirstCar = new CarClass("Steamer", 1949, "water"); // (String modelIn, int yearIn, String engineTypeIn)

        // Create other car (object)
        CarClass mySecondCar = new CarClass("HydroCar", 2026, "H2"); // (String modelIn, int yearIn, String engineTypeIn)

        System.out.println("======================================================================");

        // Show cars info
        myFirstCar.showVehicleInfo();
        mySecondCar.showVehicleInfo();

        System.out.println("======================================================================");

        // Add fuel to the cars
        myFirstCar.addFuel(10);
        myFirstCar.addFuel(5);
        int fuelLiters = myFirstCar.getFuelAmount();
        System.out.println("My " + myFirstCar.model + " got " + fuelLiters + " liters of " + myFirstCar.engineType + ".");

        mySecondCar.addFuel(50);
        fuelLiters = mySecondCar.getFuelAmount();
        System.out.println("My " + mySecondCar.model + " got " + fuelLiters + " liters of " + mySecondCar.engineType + ".");

        System.out.println("======================================================================");

        // Add miles to the cars
        myFirstCar.addKm(139);
        myFirstCar.addKm(54);
        int mileage = myFirstCar.getMileage();
        System.out.println("My " + myFirstCar.model + " travelled " + mileage + " today.");

        mySecondCar.addKm(1000);
        mileage = mySecondCar.getMileage();
        System.out.println("My " + mySecondCar.model + " travelled " + mileage + " today.");

        System.out.println("======================================================================");
        System.out.println("TRUCKS");
        System.out.println("======================================================================");


        //-------------------------------------------
        // Create a truck (object)
        TruckClass myFirstTruck = new TruckClass("FleetStar", 1960, "1 Ton");

        // Create other truck (object)
        TruckClass mySecondTruck = new TruckClass("FleetGiant", 2000, "10 Ton");

        System.out.println("======================================================================");

        // Show trucks info
        myFirstTruck.showVehicleInfo();
        mySecondTruck.showVehicleInfo();

        System.out.println("======================================================================");

        // Add fuel to the trucks
        myFirstTruck.addFuel(100);
        myFirstTruck.addFuel(56);
        fuelLiters = myFirstTruck.getFuelAmount();
        System.out.println("My " + myFirstTruck.model + " got " + fuelLiters + " liters of biodiesel.");

        mySecondTruck.addFuel(50);
        fuelLiters = mySecondTruck.getFuelAmount();
        System.out.println("My " + mySecondTruck.model + " got " + fuelLiters + " liters of biodiesel.");

        System.out.println("======================================================================");

        // Add miles to the trucks
        myFirstTruck.addKm(1549);
        myFirstTruck.addKm(89);
        mileage = myFirstTruck.getMileage();
        System.out.println("My " + myFirstTruck.model + " travelled " + mileage + " today.");

        mySecondTruck.addKm(1000);
        mileage = mySecondTruck.getMileage();
        System.out.println("My " + mySecondTruck.model + " travelled " + mileage + " today.");

        System.out.println("======================================================================");
        System.out.println("MOTORCYCLES");
        System.out.println("======================================================================");

        //-------------------------------------------
        // Create a motorcycle (object)
        MotorcycleClass myFirstMotorcycle = new MotorcycleClass("Sunshine", 1984, 60, "red"); //

        // Create other motorcycle (object)
        MotorcycleClass mySecondMotorcycle = new MotorcycleClass("Traveller", 2025, 75, "silver"); //

        System.out.println("======================================================================");

        // Show motorcycle info
        myFirstMotorcycle.showVehicleInfo();
        mySecondMotorcycle.showVehicleInfo();

        System.out.println("======================================================================");

        // Add fuel to the motorcycles
        myFirstMotorcycle.addFuel(6);
        myFirstMotorcycle.addFuel(5);
        fuelLiters = myFirstMotorcycle.getFuelAmount();
        System.out.println("My " + myFirstMotorcycle.model + " motorcycle, that is " + myFirstMotorcycle.color + ", got " + fuelLiters + " liters of petrol.");

        mySecondMotorcycle.addFuel(57);
        fuelLiters = mySecondMotorcycle.getFuelAmount();
        System.out.println("My " + mySecondMotorcycle.model + " motorcyle, that is " + myFirstMotorcycle.color + ", got " + fuelLiters + " liters of petrol.");

        System.out.println("======================================================================");


        // Add miles to the motorcycles
        myFirstMotorcycle.addKm(155);
        myFirstMotorcycle.addKm(84);
        mileage = myFirstMotorcycle.getMileage();
        System.out.println("My " + myFirstMotorcycle.model + " travelled " + mileage + " today.");

        mySecondMotorcycle.addKm(1000);
        mileage = mySecondMotorcycle.getMileage();
        System.out.println("My " + mySecondMotorcycle.model + " travelled " + mileage + " today.");

        System.out.println("======================================================================");
        System.out.println("BICYCLES");
        System.out.println("======================================================================");

        //-------------------------------------------
        // Create a bicycle (object)
        BicycleClass myFirstBicycle = new BicycleClass("Skyler", 2000, "carbon", "road");

        // Create other bicycle (object)
        BicycleClass mySecondBicycle = new BicycleClass("Marina", 2023, "titanium", "beach");

        System.out.println("======================================================================");

        // Show bicycle info
        myFirstBicycle.showVehicleInfo();
        mySecondBicycle.showVehicleInfo();

        System.out.println("======================================================================");

        myFirstBicycle.addFuel(34);
        System.out.println("======================================================================");

        // Add miles to the bicycles
        myFirstBicycle.addKm(64);
        myFirstBicycle.addKm(89);
        mileage = myFirstBicycle.getMileage();
        System.out.println("My " + myFirstBicycle.model + " travelled " + mileage + " today.");

        mySecondBicycle.addKm(100);
        mileage = mySecondBicycle.getMileage();
        System.out.println("My " + mySecondBicycle.model + " travelled " + mileage + " today.");

        System.out.println("======================================================================");


        //-------------------------------------------
        // Show different messages about the vehicles
        // Show number of cars
        System.out.println("I have " + CarClass.numberOfCars + " cars.");;

        // Show number of trucks
        System.out.println("I have " + TruckClass.numberOfTrucks + " trucks.");;

        // Show number of motorcycles
        System.out.println("I have " + MotorcycleClass.numberOfMotorcycles + " motorcycles.");;

        // Show number of bicycles
        System.out.println("I have " + BicycleClass.numberOfBicycles + " bicycles.");;

        // Show number of vehicles
        System.out.println("I have " + VehicleClass.numberOfVehicles + " vehicles in total.");;

        //-------------------------------------------------------------


        //-------------------------------------------------------------





    }

}