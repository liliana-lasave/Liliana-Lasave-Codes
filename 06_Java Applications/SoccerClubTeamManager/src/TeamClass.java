// Maintain the information for a team as well as its player list. Allow for that adding/removal of a player and printing the entire team info including players.

import java.util.ArrayList;

public class TeamClass {
    String teamName;
    String coachName;
    ArrayList<PlayerClass> playerList;

    TeamClass(String teamName, String coachName) {      // Constructor
        this.teamName = teamName;
        this.coachName = coachName;
        this.playerList = new ArrayList<>();
    }

    // Method to print info of the team
    public void printTeamInfo() {
        System.out.println("There is a team called "+ teamName + ", that has a coach named " + coachName + ".");
    }

    // Method to add players to the ArrayList
    void addPlayer(PlayerClass player) {
        playerList.add(player);
    }

    // Method to print the list of players
    public void printPlayerList() {
        System.out.println("\nList of players in the team " + teamName + ":");

        for (PlayerClass player : playerList) {
            player.printPlayerInfo();
        }
    }

    // Method to print all team info
    public void printAllTeamInfo() {
        System.out.println("--------------------");
        printTeamInfo();
        printPlayerList();
        System.out.println("--------------------");
    }

    // Delete an individual player from the teams players list, if not found, print error message
    public void deletePlayerbyName(String playerNameToRemove) {
        for(int i = 0; i < playerList.size(); i++) {
            PlayerClass playerItem = playerList.get(i);

            if (playerItem.playerName.equals(playerNameToRemove)) {     // Check if the names are exactly the same
                playerList.remove(i);
                System.out.println("The player with the name " + playerNameToRemove + " was removed.");
                return;                  // stop searching (we already removed the player)
            }
        }
    System.out.println("There is no player with the name " + playerNameToRemove + " in our club.");
    }

}





