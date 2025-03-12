// This C program continuously prompts the user for positive numbers,
// tracks the maximum and minimum values entered,
// and terminates when the user inputs 0, then displays the results if valid numbers were provided.



#include <stdio.h>
#include <limits.h>  // Needed for INT_MAX (the highest possible integer)

int main() {
    int num_input;  // Variable to store user input
    int max = 0;    // Variable to store the maximum number
    int min = INT_MAX;  // Variable to store the minimum number, initially set to the highest value


    while (1) {  // I use 1, in order to have an infinite loop unless I break it, jumping it out of it.
        printf("Please give a positive number or 0 to quit: ");
        scanf_s("%d", &num_input);

        if (num_input == 0) {
            break;
        }
        else if (num_input < 0) {
            printf("Negative numbers are invalid.\n");
        }
        else {
            // Update max if the new number is greater than the current max
            if (num_input > max) {
                max = num_input;
            }

            // Update min if the new number is smaller than the current min
            if (num_input < min) {
                min = num_input;
            }
        }
    }

    // Only display results if at least one valid number was entered
    if (min < INT_MAX) {
        printf("\nMaximum number: %d\n", max);
        printf("Minimum number: %d\n", min);
    }
    else {
        printf("\nNo valid numbers were entered.\n");
    }

    return 0;  // End of program
}
