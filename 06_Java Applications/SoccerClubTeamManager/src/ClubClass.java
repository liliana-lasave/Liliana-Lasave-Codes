// Maintains the information for a club as well as list of individual teams. Print the information for all teams, including the underlying players. Allow for the addition or removal of a team.

import java.util.ArrayList;

public class ClubClass {
    String clubName;
    String presidentName;
    String clubLocation;
    ArrayList<TeamClass> teamList = new ArrayList<>();

    ClubClass(String clubName, String presidentName, String clubLocation) {
        this.clubName = clubName;
        this.presidentName = presidentName;
        this.clubLocation = clubLocation;
    }

    // Method to see all the info of the club
    public void printClubInfo() {
        System.out.println("There is a club called " + clubName + ", that has a president named " + presidentName + ", and it is located in " + clubLocation + ".");
    }

    // Add an individual team to the team array list
    public void addTeam (TeamClass team){
        teamList.add(team);
    }

    // Method to print the list of teams
    public void printTeamList() {
        System.out.println("\nList of teams in the club " + clubName + ":");

        for (TeamClass team : teamList) {
            team.printAllTeamInfo();
        }
    }

    // Method to delete a team from the arrayList
    public void deleteTeambyName(String teamNameToRemove) {
        for(int i = 0; i < teamList.size(); i++) {
            TeamClass teamItem = teamList.get(i);

            if (teamItem.teamName.equals(teamNameToRemove)) {       // Check if the names are exactly the same
                teamList.remove(i);
                System.out.println("The team with the name " + teamNameToRemove + " was removed.");
                return;                                 // Get out of the method (it finishes here)
            }
        }
    System.out.println("There is no team with the name " + teamNameToRemove + " in our club.");
    }
}


