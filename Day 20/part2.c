#include <stdio.h>

int main(int argc, char* argv[]){
	long presents = 0;
	long house = 49;
	long start = 1;

	//Find a house with at least 36000000 presents
	while(presents < 36000000){
		presents = 0;

		//Elves will only deliver to 50 houses
		if(house % (start * 50) == 0){
			start++;
		}

		//Calculate the presents at a house
		for(long i = start; i <= house; i++){
			if(house % i == 0){
				presents += i * 11;
			}
		}

		//Print the status for every 50000 houses
		if(house % 50000 == 0){
			printf("House: %d\n", house);
		}
		
		house++;
	}

	printf("Result house: %d\n", house - 1);
	return 0;
}