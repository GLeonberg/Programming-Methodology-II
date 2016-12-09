# import matplotlib.pyplot as plt
import time

callList = []
resultsIter = []

#---------------------------------------------------------------
# hanoi
#---------------------------------------------------------------
# Solves the "Towers of Hanoi" problem recursively
# moves numDsk disks from src to dest using spare
#
# pre: 	numCalls is an integer containing zero
#		src, dest, spare are arrays of ints
#		numDsk is an integer containing the number of disks to move
#
# post: All disks moved from src to dest
#---------------------------------------------------------------
def hanoi(numDsk, src, dest, spare):

	# if we only have to move 1 disk, simply move it from src to dest
	if(numDsk == 1):

		dest.append(src.pop())
		callList.append(1)
		return
	
	# otherwise we use the recursive algorithm	
	else:
	
		hanoi(numDsk-1, src, spare, dest)
		hanoi(1, src, dest, spare)
		hanoi(numDsk-1, spare, dest, src)
		return

#---------------------------------------------------------------
# hanoiIter
#---------------------------------------------------------------
# Solves the "Towers of Hanoi" problem iteratively
# moves numDsk disks from src to dest using spare
#
# pre: 	numCalls is an integer containing zero
#		src, dest, spare are arrays of ints
#		numDsk is an integer containing the number of disks to move
#
# post: All disks moved from src to dest
#---------------------------------------------------------------
def hanoiIter(numDsk, src, dest, spare):

	totalMoves = pow(2, numDsk) - 1

	if numDsk % 2 == 0 and len(spare) > 0 and len(dest) > 0:

		temp = spare.pop()
		spare.append(dest.pop())
		dest.append(temp)

	for k in range(1, totalMoves):

		if k % 3 == 1 and len(src) > 0:
			dest.append(src.pop())
 			
		elif k % 3 == 2 and len(src) > 0:
			spare.append(src.pop())
 
		elif k % 3 == 0 and len(spare) > 0:
			dest.append(spare.pop())
	
	resultsIter.append(totalMoves)
	return
#---------------------------------------------------------------

inputs = []
results = []
timeI = []
timeR = []

for i in range(1, 25):

	callList = []
	poleA = []	
	poleB = []
	poleC = []
	poleA2 = []	
	poleB2 = []
	poleC2 = []	
	
	
	for j in range(0, i):
		poleA.append(j)
		poleA2.append(j)

	timeb = float(time.time())
	hanoi(i, poleA, poleB, poleC)
	timeb = float(time.time()) - timeb

	timeIterb = float(time.time())
	hanoiIter(i, poleA2, poleB2, poleC2)
	timeIterb = float(time.time()) - timeIterb	

	timeR.append((timeb) * 1000)
	timeI.append((timeIterb * 1000))
	inputs.append(i)
	results.append(len(callList))
	
	print "Number of disks to move: " + str(i)
	print "Number of moves: " + str(len(callList))

	print "Time spent in recursive solution (ms): " + str(timeb * 1000)
	print "Time spent in iterative solution (ms): " + str(timeIterb * 1000)

#plt.plot(inputs, results, "b-", label="Recur")
#plt.plot(inputs, resultsIter, "r-", label="Iter")
#plt.ylabel("Number of Moves")
#plt.xlabel("Number of Disks")
#plt.title("Tower of Hanoi Time Complexity wrt Input Size")
#plt.legend(loc="upper left")
#plt.figure(1)

#plt.figure(2)
#plt.plot(inputs, timeI, "b-", label="Iter")
#plt.plot(inputs, timeR, "r-", label="Recur")
#plt.ylabel("Time (ms)")
#plt.xlabel("Number of disks")
#plt.title("Tower of Hanoi Execution Time")
#plt.title("Time Comparison")
#plt.legend(loc="upper left")
#plt.figure(2)
#plt.show()
