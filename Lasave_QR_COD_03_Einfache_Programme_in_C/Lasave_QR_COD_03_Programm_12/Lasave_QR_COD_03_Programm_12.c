
// This C program calculates and prints the results of multiplying num_1 by num_2 raised to the power of i for 4 iterations, 
// then divides the final result by num_2 in reverse order for 4 iterations.


#include <stdio.h>
#include <math.h>  // For pow() function

int main() {
	int num_1 = 5;
	int num_2 = 7;
	int numloops = 4;
	int i;
	int result;

	for (int i = 1; i <= numloops; i++) {
		result = num_1 * (int)pow(num_2, i);
		printf("%d\n", result);
	}

	for (int i = 1; i <= numloops; i++) {
		result = result / num_2;
		printf("%d\n", result);
	}

	return 0;
}