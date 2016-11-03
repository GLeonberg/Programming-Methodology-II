// Gregory Leonberg

// Teller.h: defines a basic Teller class used in bank simulation

#ifndef TELLER_H
#define TELLER_H

class Teller
{
	private:

		bool empty;
		int countDown;
	
	public:

		Teller()
		{		
			empty = true;
			countDown = 0;
		};
		
		bool isEmpty()
		{	return empty;	}
		
		void setFull()
		{	empty = false;	}

		void startTimer(int time)
		{	countDown = time;	}

		void decTimer(void)
		{	
			countDown--;	

			if (countDown == 0)
				empty = true;
		}

};

#endif
