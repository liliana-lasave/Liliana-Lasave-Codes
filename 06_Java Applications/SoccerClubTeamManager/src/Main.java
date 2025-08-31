//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        // CREATE DIFFERENT OBJECTS---------------------------------------------------------------------

        // Create a club object
        ClubClass club1 = new ClubClass("Royal", "Rodriguez", "Miami");

        // Create a team object
        TeamClass team1 = new TeamClass("Champions", "Mascherano");

        // Create a second team object
        TeamClass team2 = new TeamClass("Avengers", "Maddoni");

        // Create a third team object
        TeamClass team3 = new TeamClass("Atlético Brasil", "Ribeiro Junior");

        // Create a first player object
        PlayerClass player1 = new PlayerClass("Messi", "10", 1);

        // Create a second player object
        PlayerClass player2 = new PlayerClass("Suárez", "9", 0.1);

        // Create a third player object
        PlayerClass player3 = new PlayerClass("Gonzalez", "6", 2);

        // Create a fourth player object
        PlayerClass player4 = new PlayerClass("Guidi", "1", 0.5);

        // Create a fifth player object
        PlayerClass player5 = new PlayerClass("Silva", "5", 0.8);

        // ADD OBJECTS TO ARRAYLISTS ---------------------------------------------------------------------

        // Add player to ArrayList players of team 1
        team1.addPlayer(player1);
        team1.addPlayer(player2);

        // Add player to ArrayList players of team 2
        team2.addPlayer(player3);
        team2.addPlayer(player4);

        // Add player to ArrayList players of team 3
        team3.addPlayer(player5);

        // Add team to ArrayList teams
        club1.addTeam(team1);
        club1.addTeam(team2);
        club1.addTeam(team3);

        // PRINT INFORMATION ------------------------------------------------------------------------------

        System.out.println("*******");
        // Print teams list
        club1.printTeamList();
        System.out.println("*******");

        // DELETE OBJECTS ---------------------------------------------------------------------------------
        team1.deletePlayerbyName("Suárez");
        club1.deleteTeambyName("New York FC");
        club1.deleteTeambyName("Atlético Brasil");

        // PRINT UPDATED INFORMATION ------------------------------------------------------------------------------
        System.out.println("\n\n***UPDATED INFO****");

        // Print teams list
        club1.printTeamList();
        System.out.println("*******");
    }
}