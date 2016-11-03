// Gregory Leonberg

// main.cpp: conducts the frontend for the banking project	

#include "BankSim.h"
#include <iostream>

using namespace std;

int main()
{
	int numTel, rate, freq, dur, times[6];

	// bunch or printing and getting user input
	cout << "A simple bank simulation. Customers are generated with random tasks.\n\n"
		 << "Possible tasks are:\n1. Make Account\n2. Close Account\n3. Withdraw\n4."
		 << " Deposit\n5. Check Balance\n6. Transfer Funds\n\n" << endl;

	for (int i = 1; i < 7; i++)
	{
		cout << "Enter the processing time for task " << i << ": ";
		cin >> times[i - 1];
	}

	cout << "\n\nEnter the number of tellers for the simulation: ";
	cin >> numTel;

	cout << "Enter the rate at which customers arrive (cust/unit): ";
	cin >> rate;

	cout << "Enter the frequency at which customers arrive (unit): ";
	cin >> freq;

	cout << "Enter the amount of time over which customers arrive: ";
	cin >> dur;

	cout << "\n\n";

	///////////////////////////////////////////////////////////////////////
	// for 1 teller, 10 cust per unit each unit for 10 unit,   ANSWER = 45  
	// for 2 tellers, 10 cust per unit each unit for 10 unit,  ANSWER = 20
	// for 10 tellers, 10 cust per unit each unit for 10 unit, ANSWER = 0
	///////////////////////////////////////////////////////////////////////

	// run simulation and print results
	BankSim sim = BankSim(numTel, times, freq, rate, dur);
	float avgWait = sim.simulate(1);
	cout << "\n\nAverage wait time: " << avgWait << " time units.\n\n" << endl;

	// exit program
	cout << "Press enter to continue ...";
	cin.get(); 
	cin.get();

	return 0;
}
