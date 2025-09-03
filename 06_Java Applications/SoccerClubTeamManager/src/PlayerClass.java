// Maintains the information for a single player and print that info for that player

public class PlayerClass {
    String playerName;
    String playerPosition;
    double playerSalary;        // Euros/month

    PlayerClass(String playerName, String playerPosition, double playerSalary) {        // Constructor: For each player it will store name, position and salary
        this.playerName = playerName;
        this.playerPosition = playerPosition;
        this.playerSalary = playerSalary;
    }

    // Method to print the info of the current player
    public void printPlayerInfo() {
        System.out.println("There is a player called "+ playerName + ", who is playing in position " + playerPosition + ", and makes " + playerSalary + " millions of Euros per month.");
    }

}
