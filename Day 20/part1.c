#include <stdio.h>

//Call program.exe 1 and program.exe 2 so that 2 cores can work on the problem
int main(int argc, char* argv[]){
	long presents = 0;
	long house = 500000;
	long nextHouse;
	int step = 1;
	int even = 1;

	//Determine if the CPU is working on even or odds
	if(argc > 1){
		step = 2;
		if(argv[1][0] == 50){
			house++;
			even = 0;
		}
	}
	
	//Find a house with at least 36000000 presents
	while(presents < 36000000){
		presents = 0;
		nextHouse = house + 1;

		//Calculate the presents at a house
		for(long i = 1; i < nextHouse; i++){
			if(house % i == 0){
				presents += i * 10;
			}
		}
		
		//Print the status for every 10000 houses
		if(even && house % 10000 == 0){
			printf("House: %d\n", house);
		} else if(nextHouse % 10000 == 0){
			printf("House: %d\n", house);
		}
		
		house += step;
	}

	printf("Result house: %d\n", house - step);
	return 0;
}