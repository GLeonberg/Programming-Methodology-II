// Gregory Leonberg

// tester.cpp: conducts unit, system, and acceptance tests
//             for the bank simulation project using assert()

#include "BankSim.h"
#include "Customer.h"
#include "Teller.h"

#include <iostream>
#include <assert.h>

using namespace std;

// unit tests for Teller class
void testTeller();

// unit tests for Customer class
void testCustomer();

// runs simulation against a test vector
// in doing so, is system and acceptance testing
void testBankSim();

int main()
{
	// test three classes
	testTeller();
	testCustomer();
	testBankSim();
	
	// exit successfully
	cout << "Press enter to continue ...";
	cin.get();

	return 0;
}

void testTeller()
{
	// initialize a test Teller
	Teller t = Teller();
	
	// check initial state
	assert(t.isEmpty());
	
	// set to full and check that it's full
	t.setFull();
	assert(!t.isEmpty());
	
	// check the ability to count down process time
	// and then reset to empty
	t.startTimer(2);
	t.decTimer();
	assert(!t.isEmpty());
	t.decTimer();
	assert(t.isEmpty());
	
	// success message
	cout << "Teller class passed unit testing with zero errors!\n" << endl;
}

void testCustomer()
{
	// initialize a test Customer with type 1
	Customer c = Customer(1);
	
	// assert the type is 1
	assert(c.getType() == 1);
	
	// assert the wait is 0 units
	assert(c.getWait() == 0);
	
	// wait 1 unit
	c.stand();
	// assert the wait is 1 unit
	assert(c.getWait() == 1);
	
	// success message
	cout << "Customer class passed unit testing with zero errors!\n" << endl;	
}

void testBankSim()
{
	// create and run a simulation
	int temp[6] = {1, 1, 1, 1, 1, 1};
	BankSim b = BankSim(1, temp, 1, 10, 10);
	
	// test against known case of 45
	// when 100 custs, 10 each minute for 10 minutes, 1 teller
	assert (b.simulate(0) == 45);	
	
	// create and run a second simulation
	b = BankSim(2, temp, 1, 10, 10);
	
	// test against known case of 20
	// when 100 custs, 10 each minute for 10 minutes, 2 tellers
	assert (b.simulate(0) == 20);	
	
	// create and run a second simulation
	b = BankSim(10, temp, 1, 10, 10);
	
	// test against known case of 0
	// when 100 custs, 10 each minute for 10 minutes, 10 tellers
	assert (b.simulate(0) == 0);	
	
	// success message
	cout << "BankSim class passed unit testing with zero errors!\n" << endl;
}
