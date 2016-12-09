from sys import argv
script, marker, fileName = argv
txt = open(fileName)
nums = []

for line in txt:
	nums.append(float(line))

#----------------------------------------------------------------------------------
# partition
#----------------------------------------------------------------------------------
# Partitions values in arr around arr[index]
#
# pre: arr is an array, start, end , index are indexes within arr bounds
#
# post: values in arr partitioned around value that was at arr[index]
#----------------------------------------------------------------------------------
def partition(arr, start, end, index):

	pivot = arr[index]
	print "pivot = " + str(pivot)
	left = start
	right = end-1
	done = False

	while not done:

		while left <= right and arr[left] <= pivot:
			left = left + 1

		while arr[right] >= pivot and right >=left:
			right = right -1

		if right < left:
			done = True

		else:
			temp = arr[left]
			arr[left] = arr[right]
			arr[right] = temp

	temp = arr[start]
	arr[start] = arr[right]
	arr[right] = temp

	return right

#----------------------------------------------------------------------------------
# kSmall
#----------------------------------------------------------------------------------
# Finds the kth smallest value in arr, flag used to decide pivot location
#
# pre: arr is an array, k is a number from 0 to len(arr), first and last are bounds
#
# post: values in arr partitioned around kth smallest value
#----------------------------------------------------------------------------------
def kSmall(k, arr, first, last, flag):

	if flag == 0:
		p = first # pivot at front
	else:
		p = (first + last) / 2 # pivot at middle
		
	pos = partition(arr,  first, last, p)
	
	if(k < pos - first + 1):
		return kSmall(k, arr, first, pos-1, flag)
	elif(k == pos - first + 1):
		return arr[p]
	else:
		return kSmall(k - (pos - first + 1), arr, pos + 1, last, flag)

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

print "\nkSmall using first as pivot"
print kSmall(42, nums, 0, len(nums)-1, 0) 

print "\nkSmall using middle as pivot"
print kSmall(42, nums, 0, len(nums)-1, 1) 
