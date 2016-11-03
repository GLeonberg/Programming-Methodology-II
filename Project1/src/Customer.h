// Gregory Leonberg
// NetID: gdl35
// RUID: 159-00-5392

// Customer.h: defines a basic Customer class used in bank simulation

#ifndef CUSTOMER_H
#define CUSTOMER_H

class Customer
{
	private:

		int type;
		int wait;
		
	public:
		
		Customer(int t)
		{	
			wait = 0;
			type = t;
		}

		void stand()
		{	wait++;	}

		int getWait()
		{	return wait;	}

		int getType()
		{	return type;	}
};

#endif
