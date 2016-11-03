# Gregory Leonberg
# Homework Assignment 3

# feel free to un-comment the graphing code if you have
# matplotlib and associated libraries installed

# I commented out the sorting of the last 3 datasets
# (2^16, 2^20, 2^24) simply because of the enormous
# execution time they required

#import matplotlib.pyplot as plt
from time import time

############################################
def bubble(arr):
	ret = arr
	for i in range(0, len(ret)):
		swapped = False
		for j in range(0, len(ret)-1):
			if ret[j+1] < ret[j]:
				temp = ret[j+1]
				ret[j+1] = ret[j]
				ret[j] = temp
				swapped = True
		if not swapped:
			return ret
	return ret

############################################
def selection(arr):
	ret = arr
	for i in range(0, len(ret)):
		maxPos = 0
		for j in range(0, len(ret)-i):
			if ret[j] > ret[maxPos]:
				maxPos = j
		
		temp = ret[maxPos]
		ret[maxPos] = ret[len(ret)-1-i]
		ret[len(ret)-1-i] = temp
	return ret

############################################
def insertion(arr):

	ret = []
	ret.append(arr[0])
	
	for i in range(1, len(arr)):
		cur = arr[i]
		flag = True
		for j in range(0, len(ret)):
			if cur < ret[j]:
				ret.insert(j, cur)
				flag = False
				break
		if flag:
			ret.append(cur)
	return ret

############################################
def bubbleTime(f):

	t1 = time()
	ret = bubble(f)
	t2 = time()
	return t2-t1 , ret

############################################
def insertionTime(f):

	t1 = time()
	ret = insertion(f)
	t2 = time()
	return t2-t1 , ret

############################################
def selectionTime(f):

	t1 = time()
	ret = selection(f)
	t2 = time()
	return t2-t1, ret 

############################################

inputs = [2, 4, 6, 8, 10, 12]

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
bT1, arrT1 = bubbleTime(f1)
bT2, arrT2 = bubbleTime(f2)
bT3, arrT3 = bubbleTime(f3)
bT4, arrT4 = bubbleTime(f4)
bT5, arrT5 = bubbleTime(f5)
bT6, arrT6 = bubbleTime(f6)
#bT7, arrT7 = bubbleTime(f7)
#bT8, arrT8 = bubbleTime(f8)
#bT9, arrT9 = bubbleTime(f9)

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
sT1, arrT1 = selectionTime(f1)
sT2, arrT2 = selectionTime(f2)
sT3, arrT3 = selectionTime(f3)
sT4, arrT4 = selectionTime(f4)
sT5, arrT5 = selectionTime(f5)
sT6, arrT6 = selectionTime(f6)
#sT7, arrT7 = selectionTime(f7)
#sT8, arrT8 = selectionTime(f8)
#sT9, arrT9 = selectionTime(f9)

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
iT1, arrT1 = insertionTime(f1)
iT2, arrT2 = insertionTime(f2)
iT3, arrT3 = insertionTime(f3)
iT4, arrT4 = insertionTime(f4)
iT5, arrT5 = insertionTime(f5)
iT6, arrT6 = insertionTime(f6)
#iT7, arrT7 = insertionTime(f7)
#iT8, arrT8 = insertionTime(f8)
#iT9, arrT9 = insertionTime(f9)

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
bsT1, junk = bubbleTime(arrT1)
bsT2, junk = bubbleTime(arrT2)
bsT3, junk = bubbleTime(arrT3)
bsT4, junk = bubbleTime(arrT4)
bsT5, junk = bubbleTime(arrT5)
bsT6, junk = bubbleTime(arrT6)
#bsT7, junk = bubblenTime(arrT7)
#bsT8, junk = bubbleTime(arrT8)
#bsT9, junk = bubbleTime(arrT9)

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
ssT1, junk = selectionTime(arrT1)
ssT2, junk = selectionTime(arrT2)
ssT3, junk = selectionTime(arrT3)
ssT4, junk = selectionTime(arrT4)
ssT5, junk = selectionTime(arrT5)
ssT6, junk = selectionTime(arrT6)
#ssT7, junk = selectionTime(arrT7)
#ssT8, junk = selectionTime(arrT8)
#ssT9, junk = selectionTime(arrT9)

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
isT1, junk = insertionTime(arrT1)
isT2, junk = insertionTime(arrT2)
isT3, junk = insertionTime(arrT3)
isT4, junk = insertionTime(arrT4)
isT5, junk = insertionTime(arrT5)
isT6, junk = insertionTime(arrT6)
#isT7, junk = insertionTime(arrT7)
#isT8, junk = insertionTime(arrT8)
#isT9, junk = insertionTime(arrT9)

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
# Plotting
############################################

## for unsorted data
#plt.figure(1)
#plt.plot(inputs, selectionTimes, 'b-', label='selection')
#plt.plot(inputs, insertionTimes, 'r-', label='insertion')
#plt.plot(inputs, bubbleTimes, 'g-', label='bubble')
#plt.ylabel('Time (sec)')
#plt.xlabel('Dataset Size (2^x # of ints)')
#plt.title('Performance of Sort Algortihms wrt Dataset Size')
#plt.legend(loc='upper left')

## for already sorted data
#plt.figure(2)
#plt.plot(inputs, sselectionTimes, 'b-', label='selection')
#plt.plot(inputs, sinsertionTimes, 'r-', label='insertion')
#plt.plot(inputs, sbubbleTimes, 'g-', label='bubble')
#plt.ylabel('Time (sec)')
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
#	insertion sort's time is within negligible difference from the original time
#	this is because it still has to go through every iteration of the loop
#	and do comparisons, even if it doesn't do any swaps.
#
#	selection sort's time is within negligible difference from the original time
#	this is because it still has to go through every iteration of the loop
#	and do comparisons, even if it doesn't do any swaps.
#
#	bubble sort's times all become with negligible difference from zero
#	This is because of the flag that checks for early exit when no swaps occured
#	in a given iteration, hence terminating after exactly one iteration each time
############################################
