#include <vector>
#include <ctime>
#include <cstdlib>

#define n 32 // size of first array
#define k 12 // size of second array

using namespace std;

void insert(vector <int> heap, int val);

int main()
{	
	srand(time(NULL));
	
	vector <int> heapOne, heapTwo;
			
	// build first heap with random data
	for(int i = 0; i < n; i++)
		insert(heapOne, rand() % 100);
		
	// build second heap with random data
	for(int i = 0; i < k; i++)
		insert(heapTwo, rand() % 100);
	
	// merge the two heaps
	for(int i = 0; i < heapTwo.size(); i++)
	{
		val = heapTwo[i];
		insert(heapOne, val);
	}
	
	return 0;
}

void insert(vector <int> heap, int val)
{
	int currLoc = heap.size();
	int parLoc = (currLoc - 1) / 2;
	
	heap.push_back(val);
	
	bool done = false;
	
	while(!done && (parLoc >= 0))
	{
		parLoc = (currLoc - 1) / 2;
		
		if(heap[parLoc] < heap[currLoc])
		{
			int temp = heap[parLoc];
			heap[parLoc] = heap[currLoc];
			heap[currLoc] = temp;
			
			currLoc = parLoc;
		}
		
		else
			done = true;
	}
	
	return;
}
