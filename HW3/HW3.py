# Gregory Leonberg
# Homework Assignment 3

# feel free to un-comment the graphing code if you have
# matplotlib and associated libraries installed

# I commented out the sorting of the last 3 datasets
# (2^16, 2^20, 2^24) simply because of the enormous
# execution time they required

# A single operation is defined as a comparison, swap, or insertion

#import matplotlib.pyplot as plt

############################################
def bubble(arr):
	counter = 0
	ret = arr
	for i in range(0, len(ret)):
		swapped = False
		for j in range(0, len(ret)-1):
			counter += 1
			if ret[j+1] < ret[j]:
				counter += 1
				temp = ret[j+1]
				ret[j+1] = ret[j]
				ret[j] = temp
				swapped = True
		if not swapped:
			return counter, ret
	return counter, ret

############################################
def selection(arr):
	counter = 0
	ret = arr
	for i in range(0, len(ret)):
		maxPos = 0
		for j in range(0, len(ret)-i):
			counter += 1
			if ret[j] > ret[maxPos]:
				maxPos = j
		counter += 1
		temp = ret[maxPos]
		ret[maxPos] = ret[len(ret)-1-i]
		ret[len(ret)-1-i] = temp
	return counter, ret

############################################
def insertion(arr):
	counter = 0
	ret = []
	ret.append(arr[0])
	
	for i in range(1, len(arr)):
		cur = arr[i]
		flag = True
		for j in range(0, len(ret)):
			counter += 1
			if cur < ret[j]:
				counter += 1
				ret.insert(j, cur)
				flag = False
				break
		if flag:
			counter += 1
			ret.append(cur)
	return counter, ret

############################################

# create lists to hold times
selectionTimes = []
insertionTimes = []
bubbleTimes = []
sselectionTimes = []
sinsertionTimes = []
sbubbleTimes = []

############################################
# open files and read contents into arrays
f1 = []
with open('dus-2.txt') as temp:
		for line in temp:
			f1.append(int(line.rstrip('\n')))

f2 = []
with open('dus-4.txt') as temp:
		for line in temp:
			f2.append(int(line.rstrip('\n')))

f3 = []
with open('dus-6.txt') as temp:
		for line in temp:
			f3.append(int(line.rstrip('\n')))

f4 = []
with open('dus-8.txt') as temp:
		for line in temp:
			f4.append(int(line.rstrip('\n')))

f5 = []
with open('dus-10.txt') as temp:
		for line in temp:
			f5.append(int(line.rstrip('\n')))

f6 = []
with open('dus-12.txt') as temp:
		for line in temp:
			f6.append(int(line.rstrip('\n')))

#f7 = []
#with open('dus-16.txt') as temp:
#		for line in temp:
#			f7.append(int(line.rstrip('\n')))

#f8 = []
#with open('dus-20.txt') as temp:
#		for line in temp:
#			f8.append(int(line.rstrip('\n')))

#f9 = []
#with open('dus-24.txt') as temp:
#		for line in temp:
#			f9.append(int(line.rstrip('\n')))

############################################

# time bubble sort for all dataset sizes
bT1, arrT1 = bubble(f1)
bT2, arrT2 = bubble(f2)
bT3, arrT3 = bubble(f3)
bT4, arrT4 = bubble(f4)
bT5, arrT5 = bubble(f5)
bT6, arrT6 = bubble(f6)
#bT7, arrT7 = bubble(f7)
#bT8, arrT8 = bubble(f8)
#bT9, arrT9 = bubble(f9)

# add times to list
bubbleTimes.append(bT1)
bubbleTimes.append(bT2)
bubbleTimes.append(bT3)
bubbleTimes.append(bT4)
bubbleTimes.append(bT5)
bubbleTimes.append(bT6)
#bubbleTimes.append(bT7)
#bubbleTimes.append(bT8)
#bubbleTimes.append(bT9)

# time selection sort for all dataset sizes
sT1, arrT1 = selection(f1)
sT2, arrT2 = selection(f2)
sT3, arrT3 = selection(f3)
sT4, arrT4 = selection(f4)
sT5, arrT5 = selection(f5)
sT6, arrT6 = selection(f6)
#sT7, arrT7 = selection(f7)
#sT8, arrT8 = selection(f8)
#sT9, arrT9 = selection(f9)

# add times to list
selectionTimes.append(sT1)
selectionTimes.append(sT2)
selectionTimes.append(sT3)
selectionTimes.append(sT4)
selectionTimes.append(sT5)
selectionTimes.append(sT6)
#selectionTimes.append(sT7)
#selectionTimes.append(sT8)
#selectionTimes.append(sT9)

# time insertion sort for all dataset sizes
iT1, arrT1 = insertion(f1)
iT2, arrT2 = insertion(f2)
iT3, arrT3 = insertion(f3)
iT4, arrT4 = insertion(f4)
iT5, arrT5 = insertion(f5)
iT6, arrT6 = insertion(f6)
#iT7, arrT7 = insertion(f7)
#iT8, arrT8 = insertion(f8)
#iT9, arrT9 = insertion(f9)

# add times to list
insertionTimes.append(iT1)
insertionTimes.append(iT2)
insertionTimes.append(iT3)
insertionTimes.append(iT4)
insertionTimes.append(iT5)
insertionTimes.append(iT6)
#insertionTimes.append(iT7)
#insertionTimes.append(iT8)
#insertionTimes.append(iT9)

############################################
# time sorts for already sorted lists
############################################

# bubble sort
bsT1, junk = bubble(arrT1)
bsT2, junk = bubble(arrT2)
bsT3, junk = bubble(arrT3)
bsT4, junk = bubble(arrT4)
bsT5, junk = bubble(arrT5)
bsT6, junk = bubble(arrT6)
#bsT7, junk = bubble(arrT7)
#bsT8, junk = bubble(arrT8)
#bsT9, junk = bubble(arrT9)

# add times to list
sbubbleTimes.append(bsT1)
sbubbleTimes.append(bsT2)
sbubbleTimes.append(bsT3)
sbubbleTimes.append(bsT4)
sbubbleTimes.append(bsT5)
sbubbleTimes.append(bsT6)
#sbubbleTimes.append(bsT7)
#sbubbleTimes.append(bsT8)
#sbubbleTimes.append(bsT9)

# selection sort
ssT1, junk = selection(arrT1)
ssT2, junk = selection(arrT2)
ssT3, junk = selection(arrT3)
ssT4, junk = selection(arrT4)
ssT5, junk = selection(arrT5)
ssT6, junk = selection(arrT6)
#ssT7, junk = selection(arrT7)
#ssT8, junk = selection(arrT8)
#ssT9, junk = selection(arrT9)

# add times to list
sselectionTimes.append(ssT1)
sselectionTimes.append(ssT2)
sselectionTimes.append(ssT3)
sselectionTimes.append(ssT4)
sselectionTimes.append(ssT5)
sselectionTimes.append(ssT6)
#sselectionTimes.append(ssT7)
#sselectionTimes.append(ssT8)
#sselectionTimes.append(ssT9)

# insertion sort
isT1, junk = insertion(arrT1)
isT2, junk = insertion(arrT2)
isT3, junk = insertion(arrT3)
isT4, junk = insertion(arrT4)
isT5, junk = insertion(arrT5)
isT6, junk = insertion(arrT6)
#isT7, junk = insertion(arrT7)
#isT8, junk = insertion(arrT8)
#isT9, junk = insertion(arrT9)

# add times to list
sinsertionTimes.append(isT1)
sinsertionTimes.append(isT2)
sinsertionTimes.append(isT3)
sinsertionTimes.append(isT4)
sinsertionTimes.append(isT5)
sinsertionTimes.append(isT6)
#sinsertionTimes.append(isT7)
#sinsertionTimes.append(isT8)
#sinsertionTimes.append(isT9)

############################################
# Printing results
############################################
print "Unsorted data number of operations: "
print "Selection sort: ", selectionTimes
print "Insertion sort: ", insertionTimes
print "Bubble sort: ", bubbleTimes

print "Sorted data number of operations: "
print "Selection sort: ", sselectionTimes
print "Insertion sort: ", sinsertionTimes
print "Bubble sort: ", sbubbleTimes

############################################
# Discussion (Unsorted Data Sorting)
############################################
#
# When feeding unsorted data into the algorithms:
#
#	Insertion Sort and Selection Sort take roughly the same
#	number of operations to sort the datasets.
#
#	Bubble Sort takes roughly twice as many operations as insertion and selection sort
#
#	All of the graphs have exponential, which re-affirms their O(n^2) growth rates.
############################################

############################################
# Plotting
############################################

# inputs = [2, 4, 6, 8, 10, 12]
## inputs += 16
## inputs += 20
## inputs += 24

## for unsorted data
#plt.figure(1)
#plt.plot(inputs, selectionTimes, 'b:', linewidth=9, label='selection')
#plt.plot(inputs, insertionTimes, 'r-', linewidth=4, label='insertion')
#plt.plot(inputs, bubbleTimes, 'g-', linewidth=4, label='bubble')
#plt.ylabel('Operations')
#plt.xlabel('Dataset Size (2^x # of ints)')
#plt.title('Performance of Sort Algortihms wrt Dataset Size')
#plt.legend(loc='upper left')

## for already sorted data
#plt.figure(2)
#plt.plot(inputs, sselectionTimes, 'b:', linewidth=9, label='selection')
#plt.plot(inputs, sinsertionTimes, 'r-', linewidth=4, label='insertion')
#plt.plot(inputs, sbubbleTimes, 'g-', linewidth=4, label='bubble')
#plt.ylabel('Operations')
#plt.xlabel('Dataset Size (2^x # of ints)')
#plt.title('Performance of Sort Algortihms wrt Dataset Size (already sorted data)')
#plt.legend(loc='upper left')

#plt.show()

############################################
# Discussion
############################################
#
# When feeding already sorted data into the algorithms:
#
#	Insertion sort's number of operations is exactly the same as the original.
#	This is because it still has to go through every iteration of the loop
#	and do comparisons and insertions to build the new list that gets returned.
#
#	Selection sort's number of operations is exactly the same as the original.
#	This is because it still has to go through every iteration of the loop
#	and do comparisons and swaps, even if the swap is a value with itself.
#
#	Bubble sort's number of operations all become within negligible difference from zero.
#	This is because of the flag that checks for early exit when no swaps occured
#	in a given iteration, hence terminating after exactly one iteration (n-1 operations) each time.
############################################
