// Gregory Leonberg
// NetID: gdl35
// RUID: 159-00-5392

// BankSim.h: conducts the simulation backend for the banking project

// arrRate is the number of customers that arrive in each batch
// arrFreq is how far apart in time units each batch arrives
// arrDur is how many time units customers arrive for
// processTimes is an array containing the processing times for each task

#ifndef BANKSIM_H
#define BANKSIM_H

#include <cstdio>
#include <iostream>
#include <vector>
#include <deque>
#include <ctime>
#include <cstdlib>

#include "Customer.h"
#include "Teller.h"

using namespace std;

class BankSim
{
	private:

		vector <Teller> tellers;
		deque <Customer> line;
		int arrRate, arrFreq, arrDur, totalWait, processTimes[6], simTime, numCusts;

	public:
	
// BankSim: Creates and initializes a BankSim object with which to run simulation
//-------------------------------------------------------------------------
		BankSim(int telNum, int times[6], int freq, int rate, int dur)
//-------------------------------------------------------------------------
		{
			// seed p-rng
			srand(time(NULL));

			// add tellers to bank
			for (int i = 0; i < telNum; i++)
				tellers.push_back(Teller());

			// set process times for operations
			for (int i = 0; i < 6; i++)
				processTimes[i] = times[i];

			// store other inputs for simulation
			arrRate = rate;
			arrFreq = freq;
			arrDur = dur;
			totalWait = 0;
			simTime = 0;
			numCusts = 0;
		};
		
// Tick: Simulates a single time unit of simulation
// pre: BankSim is a bank with a current time simTime 
// post: A single step of simulation has been completed
//
// accepts a flag integer to determine whether or not to print intermediate info
//-------------------------------------------------------------------------
		void tick(int print)
//-------------------------------------------------------------------------
		{

			// increment simulation time
			simTime++;

			// Customer at front tries to go to teller
			for (size_t i = 0; (i < tellers.size()) && !line.empty(); i++)
			{
				// Successful transition to teller
				if (tellers[i].isEmpty())
				{
					// print wait time and add to total wait time
					if (print == 1)
					{
						cout << "Customer go to teller ";

						printf("%2d", (int)i + 1);

						cout << " with task " << line.front().getType() + 1
							<< " at time ";

						printf("%4d", simTime);

						cout << " after wait of "
							<< line.front().getWait() << " time units." << endl;
					}

					totalWait += line.front().getWait();

					// set teller to busy and set countDown
					tellers[i].setFull();
					tellers[i].startTimer(processTimes[line.front().getType()]);
					
					// get rid of customer and exit loop
					line.pop_front();
				}
			}

			// all waiting customers increment their counter
			for (size_t i = 0; (i < line.size()) && !line.empty(); i++)
				line[i].stand();

			// all busy tellers decrement their countdown
			for (size_t i = 0; i < tellers.size(); i++)
				if (!tellers[i].isEmpty())
					tellers[i].decTimer();

		};

// Simulate: Runs the full simulation for the project
// pre: BankSim is an empty bank with starting simTime 0
// post: The full simulation has been completed (the customer line is empty and customers no longer arrive)
//
// accepts a flag integer to determine whether or not to print intermediate info
// returns the average customer wait time
//-------------------------------------------------------------------------
		float simulate(int print)
//-------------------------------------------------------------------------
		{
			for (int i = 0; i < arrDur; i++)
			{
				if(simTime % arrFreq == 0)
					for (int j = 0; j < arrRate; j++)
					{
						line.push_back(Customer(rand() % 6));
						numCusts++;
					}

				tick(print);
			}

			while (!line.empty()) tick(print);
			return float(totalWait) / numCusts;
		};
};

#endif
