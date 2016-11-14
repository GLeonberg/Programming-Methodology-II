# Gregory Leonberg
# Homework Assignment 4

# feel free to un-comment the graphing code if you have
# matplotlib and associated libraries inmqTalled

# A single operation is defined as a comparison or swap

#import matplotlib.pyplot as plt
import sys

############################################
# quick sort
############################################

# primary method
def quick(arr, left, right):

	count = 0
	
	if left < right:
		pivot, temp = partition(arr, left, right)
		count += temp
		count += quick(arr, left, pivot-1)
		count += quick(arr, pivot+1, right)
	
	return count

# helper method to partition
def partition(arr, left, right):

	
	count = 0
	
	# choose first index as pivot
	piv = arr[left]
	
	l, r = left, right
	done = False

	while not done:
	
		count += 2
		# find instance out of place on left
		while (l <= r) and arr[l] <= piv:
			count += 2
			l += 1
		
		count += 2
		# find instance out of place on right
		while (r >= l) and arr[r] >= piv:
			count += 2
			r -= 1
		
		count += 1
		# termination condition
		if r < l:
			done = True
		
		# swap left and right values that were out of place
		else:
			count += 3
			temp = arr[l]
			arr[l] = arr[r]
			arr[r] =  temp
	
	# re-insert pivot at correct location
	count += 3
	temp = arr[left]
	arr[left] = arr[r]
	arr[r] = temp
	
	return r, count

############################################
# merge sort
############################################

def merge(arr):

	count = 0
	
	if len(arr) > 1:
	
		middle = len(arr)//2

		left = arr[:middle]
		right = arr[middle:]
	
		count += merge(left)
		count += merge(right)
	
		i = 0
		j = 0
		k = 0
		
		count += 2
		while (i < len(left)) and (j < len(right)):
		
			count += 2
		
			count += 1
			if left[i] < right[j]:
				count += 1
				arr[k] = left[i]
				i += 1
			
			else:
				count += 1
				arr[k] = right[j]
				j += 1
		
			k += 1
	
		count += 1
		if i >= len(left):
			count += 1
			while j < len(right):
				count += 1
				count += 1
				arr[k] = right[j]
				j += 1
				k += 1
	
		else:
			count += 1
			while i < len(left):
				count += 1
				count += 1
				arr[k] = left[i]
				i += 1
				k += 1
	
	return count

############################################
# in place merge sort
############################################

def mergeIP(arr):
	
	count = 0
	
	blockSize = 1
	
	count += 1
	while blockSize <= len(arr):
		count += 1
		i = 0
		
		# for each pair of blocks
		for i in range(0, len(arr), blockSize*2):
			count += 1
			
			left = i # left block begin 
			middle = i + blockSize # right block begin
			
			# determing right block end
			count += 1
			if (left + 2*blockSize) > len(arr):
				right = len(arr)
			else:
				right = left + 2*blockSize
			
			# perform merge on individual pair of blocks
			l, m = left, middle
			
			# while inside each block
			count += 1
			while (l < middle) and (m < right):
				count += 1
				# if element is in right place
				count += 1
				if arr[l] < arr[m]:
					l += 1 # do nothing, go to next
					
				else:
					count += 2
					count += 3*(m-l) # m-l swaps in order to shift
					
					temp = arr[m] # store value to insert
					# shift everything in block over right one
					arr[l+1:m+1] = arr[l:m]
					arr[l] = temp # insert value in correct place
					
					l += 1
					m += 1
					middle += 1
					
		blockSize *= 2 # next size up of blocks
		
	return count

############################################

# create lists to hold times
mergeTimes = []
mergeIPTimes = []
quickTimes = []
squickTimes = []

# list of file names
names = ['dus-2.txt', 'dus-4.txt', 'dus-6.txt', 'dus-8.txt', 'dus-10.txt']
names += ['dus-12.txt', 'dus-16.txt']
names += ['dus-20.txt', 'dus-24.txt']

############################################
# perform and time quick sorting
############################################
print '\n\n'
fileCounter = 0
while fileCounter < len(names)-1:
	
	# load current file contents into list
	f = []
	with open(names[fileCounter]) as temp:
			for line in temp:
				f.append(int(line))
	
	# increase recursion depth for dus-20 and dus-24
	sys.setrecursionlimit(10000000)
	
	# perform merge sort
	print 'quick sorting', names[fileCounter]
	quickTimes.append(quick(f, 0, len(f)-1))
	print 'done quick sorting', names[fileCounter]
	print quickTimes[len(quickTimes)-1], ' operations required'
	
	print 'quick sorting sorted data'
	squickTimes.append(quick(f, 0, len(f)-1))
	print 'done quick sorting sorted data'
	print squickTimes[len(squickTimes)-1], ' operations required\n'
	fileCounter += 1
	
############################################
# perform and time merge sorting
############################################
print '\n\n'
fileCounter = 0
while fileCounter < len(names)-1:
	
	# load current file contents into list
	f = []
	with open(names[fileCounter]) as temp:
			for line in temp:
				f.append(int(line))
	
	# perform merge sort
	print 'merge sorting', names[fileCounter]
	mergeTimes.append(merge(f))
	print 'done merge sorting', names[fileCounter]
	print mergeTimes[len(mergeTimes)-1], ' operations required\n'
	fileCounter += 1

############################################
# perform and time merge in place sorting
############################################
print '\n\n'
fileCounter = 0
while fileCounter < len(names)-2:
	
	# load current file contents into list
	f = []
	with open(names[fileCounter]) as temp:
			for line in temp:
				f.append(int(line))
	
	# perform merge sort
	print 'merge in place sorting', names[fileCounter]
	mergeIPTimes.append(mergeIP(f))
	print 'done merge in place sorting', names[fileCounter]
	print mergeIPTimes[len(mergeIPTimes)-1], ' operations required\n'
	fileCounter += 1

############################################
# Printing results
############################################

print "Number of operations: "
print "Merge sort: ", mergeTimes
print "In-Place Merge sort: ", mergeIPTimes
print "Quick sort: ", quickTimes
print "Quick sort (already sorted): ", squickTimes

############################################
# Plotting
############################################

#inputs = [2, 4, 6, 8, 10, 12, 16, 20, 24]

#plt.figure(1)
#plt.plot(inputs[0:len(inputs)-1], mergeTimes, 'b-', linewidth=2)
#plt.ylabel('Operations')
#plt.xlabel('Dataset Size (2^x # of ints)')
#plt.title('Merge Sort')

#plt.figure(2)
#plt.plot(inputs[0:len(inputs)-2], mergeIPTimes, 'r-', linewidth=2)
#plt.ylabel('Operations')
#plt.xlabel('Dataset Size (2^x # of ints)')
#plt.title('Merge In Place Sort')

#plt.figure(3)
#plt.plot(inputs[0:len(inputs)-1], quickTimes, 'g-', linewidth=2)
#plt.ylabel('Operations')
#plt.xlabel('Dataset Size (2^x # of ints)')
#plt.title('Quick Sort')

#plt.figure(4)
#plt.plot(inputs[0:len(inputs)-1], squickTimes, 'g-', linewidth=2)
#plt.ylabel('Operations')
#plt.xlabel('Dataset Size (2^x # of ints)')
#plt.title('Quick Sort (already sorted data)')

#plt.show()
