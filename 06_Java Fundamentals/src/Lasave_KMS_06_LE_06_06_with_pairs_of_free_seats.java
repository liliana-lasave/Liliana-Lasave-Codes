public class Lasave_KMS_06_LE_06_06_with_pairs_of_free_seats {
    public static void main(String[] args) {

        int[][] cinema = new int[3][6];     // To create a matrix of 3 rows and 6 columns. Each element it is initialized with 0 by default.

        cinema[0][0] = 1;
        cinema[0][5] = 1;
        cinema[1][2] = 1;
        cinema[2][4] = 1;
        cinema[2][5] = 1;

        int freeSeatCounterPerTheater = 0;
        int ocuppiedSeatCounterPerTheater = 0;

        for (int i = 0; i < cinema.length; i++) {           // Go through the rows

            int freeSeatCounterPerRow = 0;
            int freePairOfSeats = 0;
            System.out.println();       // Line break

            for (int j = 0; j < cinema[i].length; j++) {    // Go through each seat in a row

                System.out.print(cinema[i][j] + " ");       // Show each seat

                if (cinema[i][j] == 0) {
                    freeSeatCounterPerRow++;
                    freeSeatCounterPerTheater++;
                }else {
                    ocuppiedSeatCounterPerTheater++;
                }

                if (j < cinema[i].length - 1 && cinema[i][j] ==0 && cinema[i][j + 1] == 0) {
                    freePairOfSeats++;
                }

            }
            System.out.println();       // Line break after each row
            System.out.println("➡️ " + freeSeatCounterPerRow + " free places in row " + i);         // Shows how many free places are in each row
            System.out.println("➡️ " + freePairOfSeats + " pair of free places in row " + i);         // Shows how many free double places are in each row

        }
        System.out.println();       // Line break
        System.out.println("👉 " + (freeSeatCounterPerTheater + ocuppiedSeatCounterPerTheater) + " total places in the theater.\n");     // Shows how many places are in the whole theater
        System.out.println("👉 " + freeSeatCounterPerTheater + " free places and " + ocuppiedSeatCounterPerTheater + " occupied places in the theater.\n");     // Shows how many free and occupied places are in the whole theater

        double occupancyRate = (double) ocuppiedSeatCounterPerTheater * 100 / (freeSeatCounterPerTheater + ocuppiedSeatCounterPerTheater);      // To avoid incorrect results if % are not integers, we use double to obtain decimals
        System.out.printf("👉 %.2f%% of the theater is occupied.\n", occupancyRate);     // Shows the occupancy rate of the theater




    }
}
