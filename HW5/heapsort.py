#import matplotlib.pyplot as pyplot

def heapInsert(heap, val):
	
	heap += [val]
	counter = 0
	
	# child and parent indexes
	counter += 2
	currInd = len(heap)-1
	parentInd = (currInd-1) // 2
	
	done = False
	
	counter += 2
	while (not currInd == 0) and not done:
		counter += 1
		if heap[currInd] > heap[parentInd]:
			counter += 1
			temp = heap[currInd]
			heap[currInd] = heap[parentInd]
			heap[parentInd] = temp
		else:
			done = True
		
		counter += 2
		currInd = parentInd
		parentInd = (currInd-1) // 2
	
	return counter

def heapPop(heap):

	counter = 0
	top = heap[0]
	
	# make bottom top and remove extra space
	heap[0] = heap[len(heap)-1]
	heap.pop(len(heap)-1)
	counter += 2
	
	newHeap = []
	
	counter += len(heap)
	for val in heap:
		heapInsert(newHeap, val)
	
	counter += len(heap)
	for i in range(len(heap)):
		heap[i] = newHeap[i]
	
	return top, counter

def heapSort(arr):
	
	tempCounter, counter, val, heap, sortedArr = 0, 0, 0, [], []
	
	# Build 'da heap
	for num in arr:
		counter += heapInsert(heap, num)
	
	# Destroy 'da heap
	for ind in range(0, len(arr)):
		val, tempCounter = heapPop(heap)
		sortedArr.append(val)
		counter += tempCounter
	
	sortedArr.reverse()
	
	return sortedArr, counter

heap = []
arr = []
times = []

# list of file names
names = ['dus-2.txt', 'dus-4.txt', 'dus-6.txt', 'dus-8.txt', 'dus-10.txt', 'dus-12.txt']
# names += ['dus-16.txt', dus-20.txt', 'dus-24.txt']

for fileName in names:
	with open(fileName) as fale:
		
		sortedArr = []
		opcount = 0
		
		for num in fale:
			sortedArr.append(int(num))
		
		sortedArr, opcount = heapSort(sortedArr)
		print opcount
		
		times.append(opcount)
		
#pyplot.figure()
#pyplot.plot(range(0, len(times)), times, 'r-')
#pyplot.title('Sorting Performance')
#pyplot.xlabel("File")
#pyplot.ylabel("Number of Operations")

#pyplot.show()
