// This code generates and prints the first 11 numbers of the Fibonacci sequence starting from 0 and 1:

#include <stdio.h>

int main() {
	int num_prev1 = 0;
	int num_prev2 = 1;
	int num_current;
	int i;
	int n = 10;

	printf(" %d\n %d\n", num_prev1, num_prev2);

	for (int i = 2; i <= n; i++) {
		num_current = num_prev1 + num_prev2;
		printf(" %d\n", num_current);

		num_prev1 = num_prev2;
		num_prev2 = num_current;
	}
	return 0;
}
