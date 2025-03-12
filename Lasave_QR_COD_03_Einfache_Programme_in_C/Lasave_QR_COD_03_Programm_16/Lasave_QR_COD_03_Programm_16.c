// This code is for finding and printing a specified number of prime numbers, starting from the first prime number (2), based on user input.

#include <stdio.h>
#include <math.h>

int main() {
	int num_evaluated = 2;  // start verifying from the first prime number
	int i;
	int counter = 0;    // coounter of found prime numbers
	int num_prime_needed;   // amount of prime numbers required by the user
	int num_is_prime;

	printf("Please give the number of prime values needed: ");
	scanf_s("%d", &num_prime_needed);

	printf("The prime numbers are: \n");

	while (1) {    // Infinite loop
		num_is_prime = 1; 		// Optimistic approach 

		// Check if the number is prime
		for (i = 2; i <= sqrt(num_evaluated); i++) {
			if (num_evaluated % i == 0) {
				num_is_prime = 0;   // Not prime
				break;
			}
		}
		// If the number is prime, print it and increment the counter
		if (num_is_prime == 1) {
			printf("%d\n", num_evaluated);
			counter++;
		}
		// Exit the loop if the required number of primes is found
		if (counter >= num_prime_needed) {
			break;
		}

		num_evaluated++;  // Move to the next number, regardless of whether the number is odd or even
	}

	return 0;
}