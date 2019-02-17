num_array = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = raw_input("num :")
    num_array.append(int(n))
print 'ARRAY: ',num_array
list = []
from sys import maxint 
def maxSequence(num_array,n): 
 max_so_far = -maxint - 1
 max_ending_here = 0
 for i in range(0, n): 
  max_ending_here = max_ending_here + num_array[i] 
  if (max_so_far < max_ending_here): 
   max_so_far = max_ending_here 
  if max_ending_here < 0: 
   max_ending_here = 0   
  if  max_so_far >= max_ending_here :
   list.append(num_array[i])
 return max_so_far 
print "Maximum continuous sum is", maxSequence(num_array, len(num_array))
print "Maximum continuous array is ",list