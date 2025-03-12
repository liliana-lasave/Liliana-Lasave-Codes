// This C program generatesand prints a sequence of values by repeatedly multiplying an initial value by a given factor, based on the number of values specified by the user.

#include <stdio.h>

int main() {
	int i;
	int num_values_needed;
	int factor;
	int current_value;
	int initial_value = 1;

	printf("Please give a number of values needed: ");
	scanf_s("%d", &num_values_needed);

	printf("Please give a factor: ");
	scanf_s("%d", &factor);

	printf("Your sequence of values is: %d\n", initial_value);

	for (i = 2; i <= num_values_needed; i++) {
		//printf("In the for loop: %d\n", i);
		current_value = initial_value * factor;
		initial_value = current_value;
		printf("                            %d\n", current_value);
	}

	return 0;
}